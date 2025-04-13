from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def site_index(request):
    template = 'nmap_site/site_index.html'
    context = {}
    return render(request, template, context)

def site_history(request):
    return render(request, "nmap_site/site_history.html")

def site_description(request):
    return render(request, "nmap_site/site_description.html")

def site_tech_details(request):
    return render(request, "nmap_site/site_details.html")

def site_tests(request):
    return render(request, "nmap_site/site_tests.html")

def site_results(request):
    return render(request, "nmap_site/site_results.html")

def site_other_tools(request):
    return render(request, "nmap_site/site_othertools.html")

def site_orchestration(request):
    return render(request, "nmap_site/site_orchestration.html")