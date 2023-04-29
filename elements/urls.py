from django.conf.urls import url
from django.urls import path

from elements.views import index,  ElementsDetailView, ElementsListView, ElementCreate, ElementsDelete, ElementsUpdate, SearchResult

urlpatterns = [
    path('', ElementsListView.as_view(), name='element_page'),
    path('search/', SearchResult.as_view(), name='search_results'),
    path('element/<int:elements_pk>/', ElementsDetailView.as_view(), name='elements-detail'),
    path('element/add', ElementsUpdate.as_view(), name='element_add'),

]

urlpatterns += [
    url(r'element/create/$', ElementCreate.as_view(), name='element_create'),
    url(r'element/update/(?P<pk>\d+)$', ElementsUpdate.as_view(), name='element_update'),
    url(r'element/delete/(?P<pk>\d+)$', ElementsDelete.as_view(), name='element_delete'),
]