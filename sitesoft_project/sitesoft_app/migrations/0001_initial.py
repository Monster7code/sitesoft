# Generated by Django 5.1 on 2024-08-30 10:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource_link', models.CharField(max_length=20, unique=True, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=70, verbose_name='Заголовок')),
                ('article_link', models.CharField(max_length=100, unique=True, verbose_name='Ссылка на статью')),
                ('date_of_publication', models.DateTimeField(verbose_name='Дата публикации')),
                ('author_link', models.CharField(max_length=100, verbose_name='Ссылка на автора')),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitesoft_app.resource', verbose_name='Хабр')),
            ],
        ),
    ]
