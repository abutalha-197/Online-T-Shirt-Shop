from django.shortcuts import redirect, render
from django.http import HttpResponse


def about(request):
    return render(request,'First_App/about.html', context={})


def contact(request):
    return render(request,'First_App/contact.html', context={})


