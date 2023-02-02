from django.db import models


# Create your models here.


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
    content = models.TextField(max_length=1000, help_text='Введите краткое описание элемента',
                               verbose_name='об элементе')
    molar_mass = models.FloatField(max_length=10, help_text='Ведите молярную массу элемента',
                                   verbose_name='молярная масса')
    characteristics = models.ForeignKey('Characteristics', on_delete=models.CASCADE, help_text='выберите характеристику',
                                   null=False, verbose_name='Характеристика', )
    period = models.ForeignKey('Period', on_delete=models.CASCADE, help_text='выберите период', null=False,
                               verbose_name='Период', )
    configuration = models.ForeignKey('Configuration', on_delete=models.CASCADE, help_text='выберите конфигурации',
                                      null=False, verbose_name='Конфигурация', )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'элементы'
        verbose_name_plural = 'элементы'



