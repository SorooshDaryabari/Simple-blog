from rest_framework import serializers
from articles.models import (
    Category,
    Post,
    PostImages,
    Comment,
    Tag
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "name",
            "slug",
            "parent",
            "is_active",
        )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            "id",
            "reply",
            "post",
            "user",
            "text",
            "created_at",
        )


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("name",)


class PostImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImages
        fields = (
            "image",
            "alt_text",
        )


class PostSerializer(serializers.ModelSerializer):
    post_image = PostImagesSerializer(many=True, read_only=True)
    post_comments = CommentSerializer(many=True, source="comment_set", read_only=True)

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "slug",
            "description",
            "category",
            "author",
            "tags",
            "updated_at",
            "post_image",
            "post_comments",
        )
