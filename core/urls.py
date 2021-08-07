from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('calculate_order_total',views.calculate_order_total, name='calculate_order_total'),
]