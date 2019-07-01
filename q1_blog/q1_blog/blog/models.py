from django.db import models

class User(models.Model):

    name = models.CharField(max_length=20)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

class Post(models.Model):

    # user = models.ForeignKey('User', on_delete=models.CASCADE)
    user_id = models.IntegerField()
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
