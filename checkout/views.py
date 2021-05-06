from django.shortcuts import render
from django.http import HttpResponse

def renderCheckoutPage(request):
    return HttpResponse('Successful Checkout')
