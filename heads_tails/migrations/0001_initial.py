# Generated by Django 4.2.6 on 2023-10-29 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HeadsTails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heads_tails', models.CharField(max_length=10)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
