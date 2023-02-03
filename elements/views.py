from django.forms import model_to_dict
from rest_framework import generics
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from elements.models import Elements
from elements.serializers import ElementsSerializer


# class ElementsAPIView(generics.ListAPIView):  # данное представление необходимо связать с определенным маршрутом
#    # определяем отрибут, кторый из таблицы Elements возьмет все записи
#    queryset = Elements.objects.all()
#    # указываем класс сериализатора, его необходимо определить в спец файле
#    serializer_class = ElementsSerializer

class ElementsAPIView(APIView):
    def get(self, request):  # обрапботка get-запросов
        e = Elements.objects.all() #формирование списков из объектов
        return Response({'posts': ElementsSerializer(e, many=True).data}) # собираем данные json

    def post(self, request):
        serializer = ElementsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        post_new = Elements.objects.create(
            name=request.data['name'],
            content=request.data['content'],
            molar_mass=request.data['molar_mass'],
            characteristics_id=request.data['characteristics_id'],
            period_id=request.data['period_id'],
            configuration_id=request.data['configuration_id'],

        )
        return Response({'post': ElementsSerializer(post_new).data})


def index(request):
    return HttpResponse('Привет')
