from django.shortcuts import render
from django.http import HttpResponse

def renderHomePage(request):
    return HttpResponse('home')

def renderAboutPage(request):
    return HttpResponse('about')

def renderContactUsPage(request):
    return HttpResponse('contact')
