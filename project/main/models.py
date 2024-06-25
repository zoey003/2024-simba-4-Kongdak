from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=50)
    subcategory = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    weather = models.CharField(max_length=10)
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)
    bookmark = models.ManyToManyField(User, related_name='bookmark', blank=True)

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=10)
    studentID = models.CharField(max_length=30, null=True)