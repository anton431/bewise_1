from rest_framework.views import APIView
from index.models import Requests
from index.serializer import IntegerSerializer, RequestSerializer
from rest_framework.response import Response
import requests
from index.utils import create_questions


class RequestsAPIView(APIView):
    def post(self, request):

        answer = Requests.objects.all()
        #Возвращает предыдущий вопрос (последний вопрос, перед добавлением нового)
        if answer:
            answer = RequestSerializer(answer, many=True).data[-1] # list[dict]
        else:
            answer = {}

        questions_num = request.data['questions_num']
        tp_api = f"https://jservice.io/api/random?count={questions_num}"
        response_data = requests.get(tp_api).json()
        my_serializer = IntegerSerializer(data=request.data)
        my_serializer.is_valid(raise_exception=True) # проверка: передали неотрицательное цело число

        for req in response_data: # идем по списку словарей
            create_questions(req) # из index.utils

        return Response({'answer': answer})



