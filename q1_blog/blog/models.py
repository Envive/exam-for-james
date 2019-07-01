from django.db import models

class User(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.EmailField()

class Post(models.Model):

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
