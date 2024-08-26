from django.shortcuts import render, redirect


def index(request):
    return render(request, 'core/index.html')

def contact(request):
    return render(request, 'core/contact.html')
