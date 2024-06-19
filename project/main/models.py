from django.db import models
from django.utils import timezone
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    place = models.CharField(max_length=10)

    def __str__(self):
        return self.place
    
class Tag(models.Model):
    name = models.CharField(max_length=30,null=False,blank=False)

    def __str__(self):
        return self.name
    
class Post(models.Model):
    writer = models.ForeignKey(User, null=False,blank=False,on_delete=models.CASCADE) 
    pub_date = models.DateTimeField()
    title = models.CharField(max_length=50)
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='pots',blank=True)
    
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