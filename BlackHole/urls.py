
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('login/', views.login),
    path('QuieneSomos/', views.QuieneSomos),
    path('tienda/', views.tienda),
    
]
