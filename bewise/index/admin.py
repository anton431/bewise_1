from django.contrib import admin

from .models import Requests


class RequestsAdmin(admin.ModelAdmin):
    list_display = ('id_question', 'text_answer', 'created_at')
    list_display_links = ('id_question',)
    search_fields = ('id_question', 'created_at')
    list_filter = ('created_at', )

admin.site.register(Requests, RequestsAdmin)
