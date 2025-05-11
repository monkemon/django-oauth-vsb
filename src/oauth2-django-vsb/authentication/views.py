import requests
import os
import time

from django.shortcuts import render, redirect

from urllib.parse import urlencode

from django.contrib.auth import login, logout
from authentication.models import CustomUser

google_auth_endpoint = "https://accounts.google.com/o/oauth2/v2/auth"

# insert secrets here for debug or set in .env file if using docker
google_client_id = os.getenv("GOOGLE_API_CLIENT_ID") or ""
google_client_secret = os.getenv("GOOGLE_API_CLIENT_SECRET") or ""

print("SECRETS")
print(google_client_id)
print(google_client_secret)

state = "Kebab"

def google_redirect(request):

    params = {
        "client_id": google_client_id,
        "redirect_uri": "http://localhost:8000/auth/google/callback",
        "response_type": "code",
        "scope": "email",
        "state": state,
        "access_type": "offline",
    }


    return redirect(f"{google_auth_endpoint}?{urlencode(params)}")

def google_callback(request):

    data = {
        "GET": request.GET,
        "POST": request.POST,
    }

    data = data[request.method]

    if data["state"] != state:
        return redirect("/login")
    
    code = data["code"]
    scope = data["scope"]


    data = {
        "client_id": google_client_id,
        "client_secret": google_client_secret,
        "code": code,
        "grant_type": "authorization_code",
        "redirect_uri": "http://localhost:8000/auth/google/callback"
    }

    res = requests.post(
        "https://oauth2.googleapis.com/token",
        data=data
    )
    # should be JSON - according to Docs
    res = res.json()

    token = res.get("access_token", None)
    if not token:
        return redirect("/login")

    user_info = requests.get(
        "https://www.googleapis.com/oauth2/v3/userinfo",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )
    user_info = user_info.json()

    request.session["user_email"] = user_info["email"]
    request.session["user_image"] = user_info["picture"]

    #----

    username = request.session["user_email"]
    picture = request.session["user_image"]
    #password = request.POST['password']

    user, created = CustomUser.objects.get_or_create(
        username=username,
        defaults={
            "username": username,
            "email": username,
            "picture": picture,
        }
    )

    if not created and user.picture != picture:
        user.picture = picture
        user.save()

    login(request, user)
    return redirect('/home')

 
def logout_view(request):
    logout(request)
    return redirect('/')
