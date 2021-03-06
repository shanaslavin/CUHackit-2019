"""Hackit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cuhackit import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('map/', views.map.as_view(), name = 'map'),
    path('', views.home_redirect, name = 'home'),
    path('api/', views.dispenser_view, name = 'api'),
    path('api/<int:dispenser_id>/', views.dispenser_view_single, name = 'api_single'),
    path('dispensed/<int:dispenser_id>/', views.dispensed_view),
    path('order_pad/<int:dispenser_id>/', views.order_pad),
    path('maintenance/', views.maintenance_view.as_view(), name = 'maintain'),
    path('maintenance/filled/<int:dispenser_id>/', views.filled_view)

]
