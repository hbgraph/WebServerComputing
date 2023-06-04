from django.contrib.auth.models import User
from django.db import models


class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    modify_count = models.IntegerField(default=0) # 수정 횟수 추가
    voter = models.ManyToManyField(User, related_name='voter_question')  # voter 추가

    def __str__(self):
        return self.subject


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    modify_count = models.IntegerField(default=0)  # 수정 횟수 추가
    voter = models.ManyToManyField(User, related_name='voter_answer')  # voter 추가

    def __str__(self):
        return self.content

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_author')
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question_modify_count = models.IntegerField(default=0)  # 질문 댓글 수정 횟수 추가
    answer_modify_count = models.IntegerField(default=0)  # 답변 댓글 수정 횟수 추가
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)
    question_voter = models.ManyToManyField(User, related_name='comment_question_voter')  # voter 추가
    answer_voter = models.ManyToManyField(User, related_name='comment_answer_voter')  # voter 추가
