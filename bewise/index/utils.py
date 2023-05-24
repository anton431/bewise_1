from index.models import Requests
import requests

from index.serializer import RequestSerializer


def create_questions(request_data):
    # выбираем нужные ключи/значения для проверки сериализатором и записи в БД
    reqw = {'id_question': request_data['id'], 'text_question': request_data['question'],
            'text_answer': request_data['answer'], 'created_at': request_data['created_at']}

    my_serializer = RequestSerializer(data=reqw)
    # если проверка прошла, в том числе уникальный id вопроса, пишем в БД
    if my_serializer.is_valid(raise_exception=True):
        Requests.objects.create(
            id_question=request_data['id'],
            text_question=request_data['question'],
            text_answer=request_data['answer'],
            created_at=request_data['created_at']
        )
    # иначе, просим еще один новый вопрос у API и повторяем те же действия
    else:
        tp_api_except = f"https://jservice.io/api/random?count=1"
        response_data = requests.get(tp_api_except).json()
        req = response_data[0]
        create_questions(req)