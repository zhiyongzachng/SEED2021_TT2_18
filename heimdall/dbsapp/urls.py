from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'), #matches empty route to here
    path('logout/', views.logout, name='logout'),
    path('overview/', views.logout, name='home-overview'),
    path('transaction/', views.logout, name='transaction'),
]
