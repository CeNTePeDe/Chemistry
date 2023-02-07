from rest_framework import serializers
from .models import Elements


class ElementsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Elements
        fields = '__all__'