from django.urls import path
from .views import *

app_name = "main"

urlpatterns=[
    path('',mainpage,name='mainpage'),
    path('new-post',new_post,name='new-post'),
    path('create',create,name='create'),
    path('edit/<int:id>',edit, name='edit'),
    path('update/<int:id>',update,name='update'),
    path('delete/<int:id>',delete,name='delete'),
    path('category/<int:category_id>/',category_posts,name='category_post'),
    path('post/<int:post_id>', post_detail, name='post_detail'),
]