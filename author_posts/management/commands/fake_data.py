from django.core.management.base import BaseCommand
from author_posts.models import Author, Article, Comment
import datetime


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("count", type=int, help="number fake authors")

    def handle(self, *args, **options):
        count = options["count"]
        for i in range(1, count + 1):
            author = Author(first_name=f"name_author_{i}",
                            last_name=f"lastname_author_{i}",
                            email=f"email_{i}_@net.do",
                            autobiography=f"many text {i}",
                            birthday=datetime.date)
            author.save()
            for j in range(1, count + 1):
                if j % 2 == 0:
                    post = Article(heading=f"heading_{j}",
                                   content=f"content_{j}_____",
                                   author=author,
                                   category=f"category__{j}__",
                                   status_publication=True)
                else:
                    post = Article(heading=f"heading_{j}",
                                   content=f"content_{j}_____",
                                   author=author,
                                   category=f"category__{j}__")
                post.save()
                for k in range(1, count + 1):
                    comment = Comment(text=f"author{i}_post{j}_comment{k}",
                                      author=author,
                                      article=post)
                    comment.save()
