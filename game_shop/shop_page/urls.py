from django.urls import path
from . import views

urlpatterns = [
    path('', views.store_page, name='store_page'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout')
]
