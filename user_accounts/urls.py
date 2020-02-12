from django.urls import path
from . import views

app_name = 'user_accounts'
urlpatterns = [
    path('', views.index, name='profile'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),

]