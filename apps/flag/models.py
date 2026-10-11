from django.db import models


class Flag(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Флаг'
        verbose_name_plural = 'Флаги'
