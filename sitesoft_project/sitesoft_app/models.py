from django.db import models


class Resource(models.Model):
    resource_link = models.CharField(unique=True, null=False, verbose_name="Название", max_length=20)

    def __str__(self):
        return self.resource_link


class Articles(models.Model):
    header = models.CharField(null=False, verbose_name="Заголовок", max_length=70)
    article_link = models.CharField(unique=True, null=False, verbose_name="Ссылка на статью", max_length=100)
    date_of_publication = models.DateTimeField(verbose_name="Дата публикации")
    author_link = models.CharField(null=False, verbose_name="Ссылка на автора", max_length=100)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, verbose_name="Хабр")
