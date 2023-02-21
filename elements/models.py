from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.urls import reverse

from Chemistry import settings


class Characteristics(models.Model):
    name = models.CharField(max_length=20, help_text='Введите характеристику элемента', verbose_name='характеристика')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'характеристика'
        verbose_name_plural = 'характеристики'


class Period(models.Model):
    name = models.IntegerField(help_text='Введите номер периода', verbose_name='период')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'период'
        verbose_name_plural = 'периоды'


class Configuration(models.Model):
    name = models.CharField(max_length=1, help_text='Введите конфигурация', verbose_name='конфигурация')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'конфигурация'
        verbose_name_plural = 'конфигурации'


class Elements(models.Model):
    name = models.CharField(max_length=20, help_text='Введите название элемента', verbose_name='элемент')
    simbol = models.CharField(max_length=5, help_text='Введите символ элемента', verbose_name='символ')
    image = models.ImageField(upload_to='element_images', null=True, blank=True, verbose_name='молярная масса')
    content = models.TextField(max_length=1000, help_text='Введите краткое описание элемента',
                               verbose_name='об элементе')
    molar_mass = models.FloatField(max_length=10, help_text='Ведите молярную массу элемента',
                                   verbose_name='молярная масса')
    characteristics = models.ForeignKey('Characteristics', on_delete=models.CASCADE,
                                        help_text='выберите характеристику',
                                        null=False, verbose_name='Характеристика', )
    period = models.ForeignKey('Period', on_delete=models.CASCADE, help_text='выберите период', null=False,
                               verbose_name='Период', )
    configuration = models.ForeignKey('Configuration', on_delete=models.CASCADE, help_text='выберите конфигурации',
                                      null=False, verbose_name='Конфигурация', )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # возращает URL-адрес для доступа к определенному экземпляру книги
        return reverse('elements-detail', kwargs={'elements_pk': self.id})

    class Meta:
        verbose_name = 'элементы'
        verbose_name_plural = 'элементы'
