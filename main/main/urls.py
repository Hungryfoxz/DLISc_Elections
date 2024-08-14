"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from app import views

urlpatterns = [
    path('admin/voting_status',views.voting_status, name='voting_status'),
    path('admin/voting_status_updates',views.voting_status_updates, name='voting_status_updates'),
    path('admin/result_status',views.result_status, name='result_status'),
    path('admin/result_status_updates',views.result_status_updates, name='result_status_updates'),
    path('admin/', admin.site.urls),
    path('',include('app.urls'))
]
