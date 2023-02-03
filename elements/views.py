from rest_framework import generics
from django.http import HttpResponse
from django.shortcuts import render

from elements.models import Elements
from elements.serializers import ElementsSerializer


class ElementsAPIView(generics.ListAPIView):  # данное представление необходимо связать с определенным маршрутом
    # определяем отрибут, кторый из таблицы Elements возьмет все записи
    queryset = Elements.objects.all()
    # указываем класс сериализатора, его необходимо определить в спец файле
    serializer_class = ElementsSerializer


def index(request):
    return HttpResponse('Привет')
