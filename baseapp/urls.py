from django.urls import path
from . import views

urlpatterns = [
    path('loginpage/', views.login_page, name='login'),
    path('logout_user/', views.logout_user, name="logout"),
    path('', views.home, name="home"),
]
