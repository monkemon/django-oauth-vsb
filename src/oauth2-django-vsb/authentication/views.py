from django.shortcuts import render, redirect

import requests

google_auth_endpoint = "https://accounts.google.com/o/oauth2/v2/auth"

def google_redirect(request):

    params = {
        "client_id": "947522629936-n6c6ic6fkej9mnho2i2hm1jg5fcu4us4.apps.googleusercontent.com",
        "redirect_uri": "http://localhost:8000/auth/google/callback",
        "response_type": "code",
        "scope": "email",
    }


    permissions = requests.get(
        url=google_auth_endpoint,
        params=params
    )

    print(permissions)

    return redirect(permissions.url)

def google_callback(request):
    return render(request, "oauth_app/site_login.html")
