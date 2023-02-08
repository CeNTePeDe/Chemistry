"""Chemistry URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include, re_path

from rest_framework import routers

from elements.views import ElementsAPIList, ElementsAPIUpdate, ElementsAPIDestroy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')), #session authentication
    path('api/v1/auth', include('djoser.urls')),
    re_path(r'^auth', include('djoser.urls.authtoken')),
    path('api/v1/elements/', ElementsAPIList.as_view()),
    path('api/v1/elements/<int:pk>/', ElementsAPIUpdate.as_view()),
    path('api/v1/elements_delete/<int:pk>/', ElementsAPIDestroy.as_view()),
    path('', include('elements.urls')),
]
