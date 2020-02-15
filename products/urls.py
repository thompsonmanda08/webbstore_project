from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('', views.products_list, name='allproducts'),
    path('register/', views.register_product, name='create'),
    path('<prod_id>/', views.product_details, name='detail'),
    path('update/<prod_id>/', views.update_product, name='update'),
    path('delete/<prod_id>', views.delete_product, name='remove'),

]
