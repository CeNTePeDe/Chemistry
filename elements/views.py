from django.forms import model_to_dict
from rest_framework import generics, viewsets
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action

from elements.models import Elements
from elements.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from elements.serializers import ElementsSerializer

class WomenAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 1000

class ElementsAPIList(generics.ListCreateAPIView):
    queryset = Elements.objects.all()
    serializer_class = ElementsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = WomenAPIListPagination

class ElementsAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Elements.objects.all()
    serializer_class = ElementsSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    authentication_classes = (TokenAuthentication, )

class ElementsAPIDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Elements.objects.all()
    serializer_class = ElementsSerializer
    permission_classes = (IsAdminOrReadOnly, )


def index(request):
    return HttpResponse('Привет')
