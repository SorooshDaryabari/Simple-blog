from django.urls import path
from articles.views import (
    CategoriesListView,
    CategoriesPostsListView,
    CategoryView,
    AuthorPostsListView,
    PostView,
    CreateCommentView,
    CommentView
)

urlpatterns = [
    path("categories/", CategoriesListView.as_view(), name="categories"),
    path("categories/<slug:slug>/", CategoryView.as_view(), name="category-view"),
    path("categories/<slug:category>/posts/", CategoriesPostsListView.as_view(), name="posts-by-category"),
    path("<str:account_id>/posts/", AuthorPostsListView.as_view(), name="posts-by-author"),
    path("posts/<slug:slug>/", PostView.as_view(), name="posts"),
    path("create-comment/", CreateCommentView.as_view(), name="create-comment"),
    path("comments/<int:id>/", CommentView.as_view(), name="comments"),
]
