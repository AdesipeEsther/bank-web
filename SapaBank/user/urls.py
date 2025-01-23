from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('transfer/', views.transfer, name='transfer'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('register/', views.register, name='register'),
    path('terms/', views.terms, name = 'terms'),
    path('privacy/', views.privacy, name = 'privacy'),
]

