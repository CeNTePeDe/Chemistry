from django.forms import model_to_dict
from rest_framework import generics, viewsets
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action

from elements.models import Elements
from elements.serializers import ElementsSerializer


class ElementsViewSet(viewsets.ModelViewSet):
    queryset = Elements.objects.all()
    serializer_class = ElementsSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not 'pk':
            return Elements.objects.all()[:3]
        return Elements.objects.filter(pk=pk)


    @action(methods=['get'], detail=False)
    def element(self, request, pk=None):
        el = Elements.objects.get(pk=pk)
        return Response({'el':el.name})


def index(request):
    return HttpResponse('Привет')
