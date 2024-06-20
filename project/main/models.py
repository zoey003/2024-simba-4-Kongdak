from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    subcategory = models.CharField(max_length=100)
    maincategory = models.CharField(max_length=100, default='default_category')

    def __str__(self):
        return f"{self.maincategory} - {self.subcategory}"



class Tag(models.Model):
    name = models.CharField(max_length=30,null=False,blank=False)

    def __str__(self):
        return self.name



class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    categories = models.ForeignKey(Category,on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name='pots',blank=True)
    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.TextField(max_length=10)
    studentID = models.TextField(null=True, max_length=30)
