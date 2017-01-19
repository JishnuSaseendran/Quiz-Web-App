
from django.db import models

class User(models.Model):
    user = models.ForeignKey('auth.User', blank=True, null=True)
    username = models.CharField(max_length = 200)
    email = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)
    choice = models.CharField(max_length=200, default=0 )
    mark = models.FloatField(default=0)

    def __str__(self):
        return self.username
    

class Questions(models.Model):
    ''' This is Model class, which contain question,choices and it's answer'''
    usernames = models.ForeignKey(User, on_delete=models.CASCADE)
    question_number = models.CharField(max_length = 2)
    question = models.CharField(max_length = 200)
    choice1 = models.CharField(max_length = 200)
    choice2 = models.CharField(max_length = 200)
    choice3 = models.CharField(max_length = 200)
    choice4 = models.CharField(max_length = 200)
    choice5 = models.CharField(max_length = 200)
    answer = models.CharField(max_length = 200)
    choice = models.CharField(max_length=200, default=0 )
    mark = models.FloatField(default=0)
    
    def __str__(self):
        return self.question


