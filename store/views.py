from django.shortcuts import render
from django.http import HttpResponse

# Site App Shopping Page view is being rendered
def renderShoppingPage(request):
    return HttpResponse('store')
