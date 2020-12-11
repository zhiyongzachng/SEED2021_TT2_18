from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'), #matches empty route to here
    path('logout/', views.logout, name='logout'),
    path('overview/', views.overview, name='home-overview'),
    path('transaction/', views.transaction, name='transaction'),
]
