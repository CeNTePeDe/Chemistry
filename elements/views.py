from django.forms import model_to_dict
from rest_framework import generics
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from elements.models import Elements
from elements.serializers import ElementsSerializer



class ElementsAPIList(generics.ListCreateAPIView): #реализует запросы GET, POST
    queryset = Elements.objects.all()
    serializer_class = ElementsSerializer


class ElementsUpdate(generics.UpdateAPIView):
    queryset = Elements.objects.all()
    serializer_class = ElementsSerializer

class ElementsAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Elements.objects.all()
    serializer_class = ElementsSerializer

def index(request):
    return HttpResponse('Привет')
