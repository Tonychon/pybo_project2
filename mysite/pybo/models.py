from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    modify_date = models.DateTimeField(null=True, blank=True) #값을 비워둘 수 있다는 의미
    create_date = models.DateTimeField()
    voter = models.ManyToManyField(User, related_name='voter_question')

    def __str__(self):
        return self.subject

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    modify_date = models.DateTimeField(null=True, blank=True)
    create_date = models.DateTimeField()
    voter = models.ManyToManyField(User, related_name='voter_answer')

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)


#p = Question(subject='pybo가 무엇인가요?', content='pybo가 알고 싶어요', create_date=timezone.now())
#p.save()
#조회
#Question.object.all() => str 메서드를 추가해서 제목을 되돌려줄 수 있게 만듬
#Question.object.filter(id=1) 조회 기능 => 쿼리셋을 보여줌, 여러개를 조회할 때 씀, 조회값이 없으면 none을 표시함
#Question.object.get(id=1) 조회 기능 => 객체를 가져옴, 1개만 조회할 때 씀, 조회값이 없으면 에러가
# Question.object.filter(subject__contains='장고') 특정 문자열이 포함된 객체를 조회, 언더바 두 개임
#수정
# q.subject = 'Django Model Question'
# q.save()
#삭제
# q = Question.objects.get(id=2)
# q.delete()
#연결 모델명
# q = Question.objects.get(id=2) 일 때
# q.answer_set.all() 하면 답변 객체들이 나옴, Answer 모델을 Question과 연결했기 때문에 => answer_set이라는 연결 객체가 가능한 것 => 모델명_set



####admin 대쉬보드 ####
#python manage.py createsuperuser