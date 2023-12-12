from django.shortcuts import render, get_object_or_404
from .models import Author as Author_model, Article as Article_model, Comment as Comment_model
from .forms import AddAuthorForm as Author_form, AddArticleForm as Article_form, AddCommentForm
import logging

logger = logging.getLogger(__name__)


def author_posts_out(request, id_author):
    author = Author_model.objects.filter(pk=id_author).first()
    posts = Article_model.objects.filter(author=author)
    context = {"author": author, "posts_author": posts}
    return render(request, "author_posts/out_posts_by_author.html", context)


def out_post(request, post_id):
    post = get_object_or_404(Article_model, pk=post_id)
    post.number_views += 1
    post.save()
    comments = Comment_model.objects.filter(article=post).order_by("-date_publication")
    # вывели все комментарии к посту
    if request.method == 'POST':
        form = AddCommentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            author = form.cleaned_data['author']
            # article = form.cleaned_data['article']
            comment = Comment_model.objects.create(
                text=text,
                author=Author_model.objects.get(pk=int(author)),
                article=post
            )
            comment.save()
    else:
        form = AddCommentForm()

    return render(request, "author_posts/post_full.html", {"post": post,
                                                           "number_views": post.number_views,
                                                           "comments": comments,
                                                           "form": form})


def add_author(request):
    if request.method == 'POST':
        form = Author_form(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            autobiography = form.cleaned_data['autobiography']
            birthday = form.cleaned_data['birthday']
            logger.info(f"get {first_name= } {last_name=} {email=} {autobiography=} {birthday=}")
            author = Author_model(first_name=first_name, last_name=last_name, email=email,
                                  autobiography=autobiography, birthday=birthday)
            author.save()
    else:
        form = Author_form()
    return render(request, 'author_posts/add_author.html', {"form": form})


def add_article(request):
    if request.method == 'POST':
        form = Article_form(request.POST)
        if form.is_valid():
            heading = form.cleaned_data['heading']
            content = form.cleaned_data['content']
            date_publication = form.cleaned_data['date_publication']
            author_id = form.cleaned_data['author']
            author = Author_model.objects.get(pk=int(author_id))
            category = form.cleaned_data['category']
            number_views = form.cleaned_data['number_views']
            status_publication = form.cleaned_data['status_publication']
            logger.info(f"{heading=} {content=} {date_publication=} {author=}"
                        f"{category=} {number_views=} {status_publication=}")
            article = Article_model(heading=heading, content=content, date_publication=date_publication,
                                    author=author,
                                    category=category,
                                    number_views=number_views,
                                    status_publication=status_publication)
            article.save()

    else:
        form = Article_form()

    return render(request, 'author_posts/add_article.html', {'form': form})
