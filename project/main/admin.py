from django.contrib import admin
from django.contrib.auth.models import User
from django.db.models import Count

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

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
