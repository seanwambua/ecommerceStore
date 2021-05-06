from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('checkout.urls')),
# Setting paths to the store app pages
    path('store/', views.renderShoppingPage,name = 'store'),
]
