from django.urls import path

from . import views


urlpatterns = [
    path('index', views.index, name='index'),
    path('registerpage',views.registerpage, name='registerpage'),
    path('register',views.register,name='register'),
    path('',views.homepage,name='homepage'),
    path('logout',views.logout,name='logout')
    

]