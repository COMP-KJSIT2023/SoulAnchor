from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Survey_filled(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False) 
    def __str__(self):
        return self.user.username
    
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    def __str__(self):
        return self.question_text

class Option(models.Model):
    option_text = models.CharField(max_length=200)
    questions = models.ManyToManyField(Question)
    def __str__(self):
        return self.option_text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"{self.question.question_text} - {self.option.option_text}"