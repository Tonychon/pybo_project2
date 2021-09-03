from django.contrib import admin
from .models import Question, Answer

#admin대쉬보드에 서치바를 추가함
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

class AnswerAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)

# Register your models here.
