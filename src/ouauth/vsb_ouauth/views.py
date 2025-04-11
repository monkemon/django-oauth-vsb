from django.shortcuts import render

def home(request):
    template = 'home/home.html'
    context = {}
    return render(request, template, context)

def bonds(request):
    template = 'bonds/bonds.html'
    context = {}
    return render(request, template, context)
