from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models. EmailField(unique=True, verbose_name='email')
    phone = models.CharField(max_length=15, verbose_name='Номер телефона', blank=True, null=True,
                             help_text='Номер телефона')
    avatar = models.ImageField(upload_to='users/avatars', blank=True, null=True, verbose_name='Аватар',
                               help_text='Загрузите аватар' )
    country = models.CharField(max_length=45, verbose_name='Страна', blank=True, null=True, help_text='Страна')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email