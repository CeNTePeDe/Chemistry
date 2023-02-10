from django.urls import path

from elements.views import index,  ElementsDetailView, ElementsListView

urlpatterns = [
    path('', ElementsListView.as_view(), name='element_page'),
    path('element/<int:elements_pk>/', ElementsDetailView.as_view(), name='elements-detail'),
]