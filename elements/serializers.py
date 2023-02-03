from rest_framework import serializers
from .models import Elements


# class ElementsSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Elements
#        fields = ('name', 'content', 'characteristics')  # это поля, которые мы будем брать для сериализации
class ElementsSerializer(serializers.Serializer):
    name = serializers.CharField()
    content = serializers.CharField()
    molar_mass = serializers.FloatField()
    characteristics_id = serializers.IntegerField()
    period_id = serializers.IntegerField()
    configuration_id = serializers.IntegerField()

    def create(self, validated_data):
        return Elements.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.content = validated_data.get('content', instance.content)
        instance.characteristics_id = validated_data.get('characteristics_id', instance.characteristics_id)
        instance.period_id = validated_data.get('period_id', instance.period_id)
        instance.configuration_id = validated_data.get('configuration_id', instance.configuration_id)
        instance.save()
        return instance