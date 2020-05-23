from django.urls import path
from CUapp import views

urlpatterns = [ 
    path('', views.index, name = 'homepage'),
    path('login/', views.loginview),
    path('logout/', views.logoutview),
    path('signup/', views.signupview),
    ]
