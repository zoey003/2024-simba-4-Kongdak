from django.db import models
from django.utils import timezone
from django.utils.timezone import now

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Post(models.Model):
    pub_date = models.DateTimeField()
    title = models.CharField(max_length=50)
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

''' 날씨 옵션 선택
    WEATHER_CHOICES = [
        ('sunny', '맑음'),
        ('bad', '나쁨'),
    ]
    weather = models.CharField(
        max_length=5,
        choices=WEATHER_CHOICES,
        default='sunny',
    )
'''