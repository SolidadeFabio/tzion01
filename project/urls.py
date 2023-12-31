from django.urls import path
from project import views

urlpatterns = [
    path('', views.home, name="home"),
    # PRODUCTS -------------------------------------------------------
    path('show_products/', views.show_products, name='show_products'),
    path('detail_product/<int:id>/', views.detail_product, name='detail_product'),
    path('create_product_page/', views.create_product_page, name='create_product_page'),
    path('create_product/', views.create_product, name='create_product'),
    path('product_json/', views.product_json, name='product_json'),
    
    # SUPPLIERS ----------------------
    path('create_supplier/', views.create_supplier, name='create_supplier')  
]