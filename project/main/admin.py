from django.contrib import admin
from django.contrib.auth.models import User
from django.db.models import Count
from .models import Post

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'post_count')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(post_count=Count('post'))
        return queryset

    def post_count(self, obj):
        return obj.post_count
    post_count.admin_order_field = 'post_count'
    post_count.short_description = 'Number of Posts'

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'subcategory', 'created_at')
    list_filter = ('category', 'subcategory')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)  # Post 모델을 PostAdmin으로 등록
