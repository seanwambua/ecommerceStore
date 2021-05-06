from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    #Creating a path to the store from the website app
    path('', include('store.urls')),
    # Setting paths to the default site app pages
    path('', views.renderHomePage,name = 'homePage'),
    path('about/',views.renderAboutPage,name = 'aboutPage'),
    path('contact/', views.renderContactUsPage,name = 'contactPage'),
]
