from django.db import models


class Settings(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название сайта')
    description = models.TextField(verbose_name='Описание сайта')
    logo = models.ImageField(upload_to='logo/', verbose_name='Логотип')
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Email')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Настройки сайта'
        verbose_name_plural = 'Настройки сайта'

