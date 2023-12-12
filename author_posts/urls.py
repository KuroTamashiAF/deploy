from django.urls import path
from .views import author_posts_out, out_post, add_author, add_article

urlpatterns = [
    path("allPosts/<int:id_author>/", author_posts_out, name="author_posts_out"),
    path("onePost/<int:post_id>/", out_post, name="out_post"),
    path("addAuthor/", add_author, name="add_author"),
    path("addArticle/", add_article, name="add_article"),

]
