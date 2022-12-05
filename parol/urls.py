from django.urls import path
from parol import views


urlpatterns = [
    path('', views.password_home, name='password_home'),
    path('password/', views.password, name='password'),
]