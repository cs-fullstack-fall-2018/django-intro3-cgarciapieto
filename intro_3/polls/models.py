from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
import datetime


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

def __str__(self):
    return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Book(models.Model):

    fields_name = models.CharField(max_length=200)
    stars = models.IntegerField(default=0)
    release_date = models.IntegerField(default=0)
    cuurent_date = models.DateField(datetime)


    def __str__(self):
        return self.book_text
