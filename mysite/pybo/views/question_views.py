from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..form import QuestionForm
from ..models import Question

@login_required(login_url='common:login') #로그인이 안되면 해당 url로 자동 이동함
def question_create(request):
    """
    질문등록
    """
    if request.method == 'POST':
        form = QuestionForm(request.POST) #post방식일 때 = 값을 넣어서 등록 했을 때, 그 값을 받아서 form 에 넣는다. post대문자로!
        if form.is_valid():
            question = form.save(commit=False) #form에 들어온 값을 question에 넣는데, create_date값이 없으므로 임시저장 false 함.
            question.author = request.user  # author 속성에 로그인 계정 저장
            question.create_date = timezone.now() #그다음 create_date값을 넣어주고
            question.save() #최종으로 모델에 저장함.
            return redirect('pybo:index')
    else: #post로 요청하지 않았을 때 => 즉 답변을 작성하기 전 링크로 들어왔을 때 (GET방식)
        form = QuestionForm() #폼을 생성함
    context = {'form':form}
    return render(request, 'pybo/question_form.html', context)

@login_required(login_url='common:login') #로그인이 안되면 해당 url로 자동 이동함
def question_modify(request, question_id):
    """
    pybo 질문 수정
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정 권한이 없습니다.')
        return redirect('pybo:detail', question_id=question_id)

    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now()
            question.save()
            return redirect('pybo:detail', question_id=question_id)
    else:
        form = QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)

@login_required(login_url='common:login')
def question_delete(request, question_id):
    """
    pybo 질문삭제
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('pybo:detail', question_id=question.id)
    question.delete()
    return redirect('pybo:index')