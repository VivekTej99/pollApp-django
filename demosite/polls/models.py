from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date_published')

    def __str__(self) -> str:
        return f"<Question(question_text={self.question_text},\
                date_published={self.pub_date}\
                )"

class Choice(models.Model):
    choice_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"<Choice(choice_text={self.choice_text},\
                votes={self.votes}\
                )"

