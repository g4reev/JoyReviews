from django.db import models

class YamapCompany(models.Model):
    title = models.CharField('Заголовок', max_length=256)
    proof_link = models.URLField(
        'Ссылка в яндекс картах накомпанию',
        max_length=2048
    )
    adress = models.CharField('Адрес', max_length=256, blank=True)
    category = models.CharField('Категория', max_length=256, blank=True)
    latitude = models.CharField('Широта', max_length=256, blank=True)
    longitude = models.CharField('Долгота', max_length=256, blank=True)
    date_time_polled = models.DateField(
        'Дата последнего опроса компании',
        blank=True,
        null=True
    )

