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
        serializer.save()

        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({"error":"Method Put not ellowed"})

        try:
            instance = Elements.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})
        serializer = ElementsSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        return Response({'post': serializer.data})



def index(request):
    return HttpResponse('Привет')
