from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('', views.products_list, name='allproducts'),
    path('register/', views.register_product, name='create'),
    path('<prod_id>/', views.product_details, name='detail'),
    path('<prod_id>/update/', views.update_product, name='update'),
    path('<prod_id>/delete/', views.delete_product, name='remove'),

]
