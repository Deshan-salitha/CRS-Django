from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),
    path('page1/', views.single_user_registration, name='singleuserregistration'),
    path('page2/', views.group_registration, name='groupregistration'),
]
