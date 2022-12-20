from rest_framework import generics
from articles.models import (
    Category,
    Post,
    Comment
)
from rest_framework.permissions import IsAuthenticated
from articles.permissions import (
    IsStaffOrReadOnly,
    IsAuthorOrReadOnly,
    IsCommentCreator
)
from articles.serializers import (
    CategorySerializer,
    PostSerializer,
    CommentSerializer
)


class CategoriesListView(generics.ListCreateAPIView):
    queryset = Category.objects.filter(is_active=True)
    permission_classes = (IsStaffOrReadOnly,)
    serializer_class = CategorySerializer


class CategoriesPostsListView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = (IsStaffOrReadOnly,)

    def get_queryset(self):
        category = self.kwargs.get("category")
        return Post.objects.filter(
            category__slug__iexact=category,
            post_status="A",
        )


class CategoryView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    permission_classes = (IsStaffOrReadOnly,)
    queryset = Category.objects.all()
    lookup_field = "slug"


class AuthorPostsListView(generics.ListCreateAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        author = self.kwargs.get("account_id")
        return Post.objects.filter(
            author__account_id__iexact=author,
            post_status="A"
        )


class PostView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.filter(post_status="A")
    lookup_field = "slug"


class CreateCommentView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Comment.objects.all()


class CommentView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    permission_classes = (IsCommentCreator,)
    queryset = Comment.objects.all()
    lookup_field = "id"
