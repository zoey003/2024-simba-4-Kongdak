from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.firstpage, name='firstpage'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('mainpage/', views.mainpage, name='mainpage'),
    path('secondpage_a/', views.secondpage_a, name='secondpage_a'),
    path('secondpage_b/', views.secondpage_b, name='secondpage_b'),
    path('secondpage_c/', views.secondpage_c, name='secondpage_c'),
    path('category/<str:category>/<str:subcategory>/', views.categorypage, name='categorypage'),
    path('category/<str:category>/<str:subcategory>/post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('category/<str:category>/<str:subcategory>/create/', views.create_post, name='create_post'),
    path('category/<str:category>/<str:subcategory>/post/<int:post_id>/edit/', views.edit_post, name='edit_post'),
    path('category/<str:category>/<str:subcategory>/post/<int:post_id>/delete/', views.delete_post, name='delete_post'),
    path('all_posts/', views.all_posts, name='all_posts'),    
    path('', auth_views.LogoutView.as_view(next_page='firstpage'), name='logout'),
    path('post/<int:post_id>/bookmark/', views.bookmark, name='bookmark'),
    path('search/tag/', views.search_by_tag, name='search_by_tag'),

