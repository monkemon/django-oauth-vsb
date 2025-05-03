from django.shortcuts import render

def site_login(request):
    return render(request, "oauth_app/site_login.html")

def site_index(request):
    if request.user.is_authenticated:
        return render(request, "oauth_app/site_index.html")
    else:
        return render(request, "oauth_app/site_login.html")

def site_history(request):
    if request.user.is_authenticated:
        return render(request, "oauth_app/site_history.html")
    else:
        return render(request, "oauth_app/site_login.html")

def site_description(request):
    if request.user.is_authenticated:
        return render(request, "oauth_app/site_description.html")
    else:
        return render(request, "oauth_app/site_login.html")
    
def site_tech_details(request):
    if request.user.is_authenticated:
        return render(request, "oauth_app/site_details.html")
    else:
        return render(request, "oauth_app/site_login.html")
    
def site_tests(request):
    if request.user.is_authenticated:
        return render(request, "oauth_app/site_tests.html")
    else:
        return render(request, "oauth_app/site_login.html")
    
def site_results(request):
    if request.user.is_authenticated:
        return render(request, "oauth_app/site_results.html")
    else:
        return render(request, "oauth_app/site_login.html")
    
def site_other_tools(request):
    if request.user.is_authenticated:
        return render(request, "oauth_app/site_othertools.html")
    else:
        return render(request, "oauth_app/site_login.html")
    
def site_orchestration(request):
    if request.user.is_authenticated:
        return render(request, "oauth_app/site_orchestration.html")
    else:
        return render(request, "oauth_app/site_login.html")