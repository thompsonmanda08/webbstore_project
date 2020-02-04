from django.urls import path
from . import views

urlpatterns = [
    path('', views.products_list),
    path('<prod_id>/', views.product_details),
    path('register_product/', views.register_product),
    path('<prod_id>/update_product/', views.update_product),
    path('<prod_id>/update_product/', views.delete_product),

]
