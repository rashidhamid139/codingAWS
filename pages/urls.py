from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('about/', views.about_view, name='about_view'),
    path('contact/', views.contact_view, name='contact_view'),
    path('social/', views.social_view, name='social_view'),
]