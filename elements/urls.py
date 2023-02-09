from django.urls import path

from elements.views import index, element_page

urlpatterns = [
    path('/', element_page, name='element_page'),
]