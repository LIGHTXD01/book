from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.books, name='books'),
    path('about/', views.libo, name='about'),
    path('events/', views.events, name='events'),
    path('contact/', views.contacts, name='contacts'),
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
]