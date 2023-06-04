from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from ..models import Question, Answer, Comment


@login_required(login_url='common:login')
def vote_question(request, question_id):
    """
    pybo 질문 추천 등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.author:
        messages.error(request, '본인이 작성한 글은 추천할 수 없습니다')
    else:
        question.voter.add(request.user)
    return redirect('pybo:detail', question_id=question.id)

@login_required(login_url='common:login')
def vote_answer(request, answer_id):
    """
    pybo 답글 추천 등록
    """
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user == answer.author:
        messages.error(request, '본인이 작성한 글은 추천할 수 없습니다')
    else:
        answer.voter.add(request.user)
    return redirect('pybo:detail', question_id=answer.question.id)

@login_required(login_url='common:login')
def question_vote_comment(request, comment_id):
    """
    pybo 질문 답글 추천 등록
    """
    question_comment = get_object_or_404(Comment, pk=comment_id)
    if request.user == question_comment.author:
        messages.error(request, '본인이 작성한 글은 추천할 수 없습니다')
    else:
        question_comment.question_voter.add(request.user)
    question = question_comment.question if question_comment.question else question_comment.answer.question
    return redirect('pybo:detail', question_id=question.id)

@login_required(login_url='common:login')
def answer_vote_comment(request, comment_id):
    """
    pybo 답변 답글 추천 등록
    """
    answer_comment = get_object_or_404(Comment, pk=comment_id)
    if request.user == answer_comment.author:
        messages.error(request, '본인이 작성한 글은 추천할 수 없습니다')
    else:
        answer_comment.answer_voter.add(request.user)
    question = answer_comment.answer.question if answer_comment.answer else answer_comment.question
    return redirect('pybo:detail', question_id=question.id)