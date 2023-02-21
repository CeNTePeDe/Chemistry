from django.db import models

from Chemistry import settings
from users.models import User


class Rubric(models.Model):
    name = models.CharField(max_length=100, verbose_name='Введите тему')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'


class Key_word(models.Model):
    words = models.CharField(max_length=20, verbose_name='Ключевые слова')

    def __str__(self):
        return self.words

    class Meta:
        verbose_name = 'Cлово'
        verbose_name_plural = 'Слова'


class Articles(models.Model):
    title = models.CharField(max_length=100, verbose_name='Введите название статьи')
    content = models.TextField(verbose_name='Введите содержание статьи')
    published = models.DateField(verbose_name='Введите дату публикации', auto_now=True)
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False,
                               verbose_name='Имя Автора')
    rubrics = models.ManyToManyField('Rubric',verbose_name='выбирите тему')
    key_words = models.ManyToManyField('Key_word', verbose_name='выбирите ключевые слова')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published']
