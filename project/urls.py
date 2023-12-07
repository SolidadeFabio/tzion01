from django.urls import path
from project import views

urlpatterns = [
    path('', views.home, name="home"),
    path('show_product', views.show_product, name='show_product'),
    path('create_product', views.create_product, name='create_product')
]