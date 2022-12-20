from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from articles.models import (
    Category,
    Post,
    Comment,
    PostImages,
    Tag
)

admin.site.register(Category, MPTTModelAdmin)


class PostImagesInline(admin.TabularInline):
    model = PostImages


class PostCommentsInline(admin.TabularInline):
    model = Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [
        PostImagesInline,
    ]


admin.site.register(Comment)
admin.site.register(Tag)
