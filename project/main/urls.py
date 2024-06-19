from django.urls import path,include
from .views import *
from main import views
app_name = "main"

urlpatterns=[
    path('', views.firstpage, name='firstpage'),
    path('mainpage/', views.mainpage, name='mainpage'),
    path('secondpage_a/', views.secondpage_a, name='secondpage_a'),
    path('secondpage_b/', views.secondpage_b, name='secondpage_b'),
    path('secondpage_c/', views.secondpage_c, name='secondpage_c'),
    path('category/<str:category>/<str:subcategory>/', views.categorypage, name='categorypage'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('category/<str:category>/<str:subcategory>/create/', views.create_post, name='create_post'),
    path('accounts/', include('accounts.urls')),
]