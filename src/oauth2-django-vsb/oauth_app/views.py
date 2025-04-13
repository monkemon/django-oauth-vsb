from django.shortcuts import render

def site_index(request):
    return render(request, "oauth_app/site_index.html")

def site_history(request):
    return render(request, "oauth_app/site_history.html")

def site_description(request):
    return render(request, "oauth_app/site_description.html")

def site_tech_details(request):
    return render(request, "oauth_app/site_details.html")

def site_tests(request):
    return render(request, "oauth_app/site_tests.html")

def site_results(request):
    return render(request, "oauth_app/site_results.html")

def site_other_tools(request):
    return render(request, "oauth_app/site_othertools.html")

def site_orchestration(request):
    return render(request, "oauth_app/site_orchestration.html")