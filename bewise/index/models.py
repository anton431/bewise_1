from django.db import models

class Requests(models.Model):
    id_question = models.PositiveIntegerField(verbose_name='ID', unique=True)
    text_question = models.CharField(verbose_name='Текст ответа', max_length=700,)
    text_answer = models.CharField(verbose_name='Текст вопроса', max_length=700)
    created_at = models.DateTimeField(verbose_name='Дата создания вопроса')

    class Meta:
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросы'

    def __str__(self):
        return self.text_question
