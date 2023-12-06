from django.urls import path
from project import views

urlpatterns = [
    path('', views.home, name="home"),
    path('product', views.product_home, name='product'),
]