from django.core.management.base import BaseCommand
from heads_tails.models import Author, Article
import datetime


class Command(BaseCommand):
    help = " "

    def add_arguments(self, parser):
        parser.add_argument('n', type=int, help="stop point")

    def handle(self, *args, **options):
        n = options['n']
        for i in range(n):
            author = Author(first_name=f"{i}", last_name=f"{i}",
                            email=f"{i}@mail.ru",
                            autobiography=f'{i} text,',
                            birthday=datetime.datetime.now())
            author.save()
            # self.stdout.write(author)

            for j in range(n):
                article = Article(heading=f"{j}", content=f"{j} many text",
                                  author=author,
                                  category=f'{j} category',
                                  )
                article.save()
