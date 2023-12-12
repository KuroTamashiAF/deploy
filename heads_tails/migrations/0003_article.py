# Generated by Django 4.2.6 on 2023-10-30 00:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('heads_tails', '0002_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('date_publication', models.DateField(auto_now_add=True)),
                ('category', models.CharField(max_length=100)),
                ('number_views', models.IntegerField(default=0)),
                ('status_publication', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='heads_tails.author')),
            ],
        ),
    ]
