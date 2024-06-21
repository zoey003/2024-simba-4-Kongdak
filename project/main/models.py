from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=30,null=False,blank=False)

    def __str__(self):
        return self.name

class Post(models.Model):
    WEATHER_CHOICES = [
    ('sunny', '맑음'),
    ('cloudy', '흐림'),
    ('rainy', '비'),
    ('snowy', '눈'),
    ]   
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=50)
    subcategory = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    weather = models.CharField(max_length=10, choices=WEATHER_CHOICES, default='sunny')
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.TextField(max_length=10)
    studentID = models.TextField(null=True, max_length=30)