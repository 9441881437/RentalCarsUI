from . import views
from django.urls import path

urlpatterns = [
    path('greet/', views.greet),
    path('', views.login, name='login_page2'),
    path('index/', views.index, name='index'),
    path('signup/', views.register, name='register'),
    path('cars_page/', views.car_booking, name='cars_page')
    
]