from django import forms
from .models import Question, Answer, Comment

class QuestionForm(forms.ModelForm): #ModelFOrm은 모델에 저장하는 폼, Form은 그냥 폼
    class Meta:
        model = Question
        fields = ['subject', 'content'] #모델의 속성값 *텍스트면 텍스트 .. 알아서 input형 폼 형태로 만듬
        # widgets = {
        #     'subject': forms.TextInput(attrs={'class': 'form-control'}),
        #     'content': forms.Textarea(attrs={'class': 'form-control', 'rows':10}),
        # } #부트스트랩 클래스를 활용한 디자인, html에서 form.as_p 처럼 값을 바로 받아서 쓸 때 쓴다.
        labels = {
            'subject' : '제목',
            'content' : '내용',
        } #번역!

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content':'답변내용',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }