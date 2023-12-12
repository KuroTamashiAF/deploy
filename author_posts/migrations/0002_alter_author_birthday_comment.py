# Generated by Django 4.2.6 on 2023-11-15 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('author_posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='birthday',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_publication', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='author_posts.article')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='author_posts.author')),
            ],
        ),
    ]
