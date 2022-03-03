from django.urls import path
from . import views

urlpatterns = [
    path('loginpage/', views.login_page, name='login'),
    path('logout_user/', views.logout_user, name="logout"),
    path('', views.home, name="home"),
    path('employeedisplay/', views.employeedatadisplay, name='employeedisplay'),
    path('addemployee/', views.addNewEmployee, name='addemployee'),
    path('editemployee/<str:pk>/', views.editEmployee, name='editemployee'),
    path('deleteemployee/<str:pk>', views.deleteEmployee, name='deleteemployee'),
    path('projectdisplay', views.projectsDisplay, name='projectdisplay'),
    path('addproject/', views.addNewProject, name='addproject'),
    path('editproject/<str:pk>/', views.editProject, name='editproject'),
    path('deleteproject/<str:pk>', views.deleteProject, name='deleteproject'),
]
