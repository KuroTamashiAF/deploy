from django import forms
from .models import Author as Author_model, Article as Article_model, Comment


def list_tuple_created():
    authors = Author_model.objects.all()
    result = []
    for author in authors:
        result.append((author.pk, author.first_name))
    return result


class AddAuthorForm(forms.Form):
    first_name = forms.CharField(min_length=1, max_length=20)
    last_name = forms.CharField(min_length=1, max_length=20)
    email = forms.EmailField()
    autobiography = forms.CharField(min_length=0, max_length=700)
    birthday = forms.DateField()


class AddArticleForm(forms.Form):
    heading = forms.CharField(min_length=0, max_length=100)
    content = forms.CharField(max_length=1000, min_length=50)
    date_publication = forms.DateField()
    author = forms.ChoiceField(choices=list_tuple_created())
    category = forms.CharField(min_length=0, max_length=100)
    number_views = forms.IntegerField()
    status_publication = forms.BooleanField(required=False)


class AddCommentForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    author = forms.ChoiceField(choices=list_tuple_created())
