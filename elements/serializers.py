from rest_framework import serializers
from .models import Elements


class ElementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elements
        #fields = ('name', 'content', 'molar_mass', 'characteristics', 'period', 'configuration')
        fields = '__all__'