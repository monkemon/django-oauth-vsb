from django.shortcuts import render

def site_login(request):
    return render(request, "oauth_app/site_login.html")

def site_index(request):
    if request.user.is_authenticated:
        return render(request, "oauth_app/site_index.html")
    else:
        return render(request, "oauth_app/site_login.html")

def site_implementation(request):
    if request.user.is_authenticated:
        return render(request, "oauth_app/site_implementation.html")
    else:
        return render(request, "oauth_app/site_login.html")
    
def site_googleCloud(request):
    if request.user.is_authenticated:
        return render(request, "oauth_app/site_googleCloud.html")
    else:
        return render(request, "oauth_app/site_login.html")
