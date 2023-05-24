from rest_framework import serializers


class RequestSerializer(serializers.Serializer):
    id_question = serializers.IntegerField()
    text_question = serializers.CharField()
    text_answer = serializers.CharField()
    created_at = serializers.DateTimeField()

class IntegerSerializer(serializers.Serializer):
    questions_num = serializers.IntegerField(min_value=1)