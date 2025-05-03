import requests

from django.shortcuts import render, redirect

from urllib.parse import urlencode

google_auth_endpoint = "https://accounts.google.com/o/oauth2/v2/auth"

state = "Kebab"

def google_redirect(request):

    params = {
        "client_id": "947522629936-n6c6ic6fkej9mnho2i2hm1jg5fcu4us4.apps.googleusercontent.com",
        "redirect_uri": "http://localhost:8000/auth/google/callback",
        "response_type": "code",
        "scope": "email",
        "state": state,
        "access_type": "offline",
    }


    return redirect(f"{google_auth_endpoint}?{urlencode(params)}")

def google_callback(request):

    print()


    return render(request, "oauth_app/site_login.html")
