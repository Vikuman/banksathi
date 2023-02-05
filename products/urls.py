
from django.urls import path
from products import views

urlpatterns = [
    path('items', views.get_products),
]
