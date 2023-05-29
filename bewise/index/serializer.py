from rest_framework import serializers
from index.models import Requests


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requests
        fields = ('__all__')

class IntegerSerializer(serializers.Serializer):
    questions_num = serializers.IntegerField(min_value=1)