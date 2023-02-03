from rest_framework import serializers
from .models import Elements


class ElementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elements
        fields = ('name', 'content', 'characteristics')  # это поля, которые мы будем брать для сериализации
