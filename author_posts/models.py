from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    autobiography = models.TextField()
    birthday = models.DateField(auto_now_add=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email} {self.birthday}"


class Article(models.Model):
    heading = models.CharField(max_length=200)
    content = models.TextField()
    date_publication = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    number_views = models.PositiveSmallIntegerField(default=0)
    status_publication = models.BooleanField(default=False)


class Comment(models.Model):
    text = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.text} {self.date_publication} {self.author} {self.article}"
