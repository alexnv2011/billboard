from django.contrib import admin
from .models import Category, Post, Reply
from django_summernote.admin import SummernoteModelAdmin


# Apply summernote to all TextField in model.
class PostAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = ('text',)


admin.site.register(Post, PostAdmin)


# Register your models here.
admin.site.register(Category)
#   admin.site.register(Post)
admin.site.register(Reply)
