from django.contrib.auth.models import AbstractUser
from django.db import models

from yam_reviews.models import YamapCompany


class User(AbstractUser):
    telegram_id = models.BigIntegerField(
        unique=True,
        verbose_name='Id пользователя телеграм'
    )
    username = models.CharField(
        max_length=32,
        blank=True,
        verbose_name='Телеграм никнейм'
    )
    first_name = models.CharField(
        max_length=64,
        blank=True,
        verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=64,
        blank=True,
        verbose_name='Фамилия'
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата регистрации'
    )
    password = models.CharField(
        max_length=128,
        blank=True,
        verbose_name='Пароль'
    )
    yam_company = models.ForeignKey(
        YamapCompany,
        on_delete=models.PROTECT,
        verbose_name='компания',
        related_name='company',
        null=True,
        blank=True
    )
    city = models.CharField(
        max_length=128,
        blank=True,
        verbose_name='Город'
    )
    USERNAME_FIELD = 'telegram_id'
    REQUIRED_FIELDS = ['username']

    class Meta:
        ordering = ['id']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return str(self.get_username())
