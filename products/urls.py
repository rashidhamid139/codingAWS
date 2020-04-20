from django.urls import path
from .import views

urlpatterns = [
    path('product/', views.product_detail_view, name='detail-view'),
    path('create/', views.product_create_view, name='create-view'),
]