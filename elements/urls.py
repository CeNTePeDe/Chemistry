from django.urls import path

from elements.views import index

urlpatterns = [
    path('', index),
]