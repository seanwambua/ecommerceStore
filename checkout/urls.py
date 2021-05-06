from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # Setting paths to the checkout app pages
    path('checkout/', views.renderCheckoutPage,name = 'checkout'),
]
