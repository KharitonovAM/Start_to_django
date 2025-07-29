import os
import secrets

from django.contrib.auth import login
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from users.forms import UserRegisterForm
from users.models import User

from config.settings import EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_USE_TLS, EMAIL_USE_SSL
from .forms import UserForm
class UserCreateView(CreateView):


    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')


    def form_valid(self, form):
        object = form.save()
        receiver_email = object.email
        host = EMAIL_HOST
        send_mail('Тема', 'Тело письма', EMAIL_HOST_USER, ['kharitonov_am@bk.ru'])
        send_mail(
            subject="Уведомление о регистрации",
            message='Поздравляю. вы зарегистрировались у нас на сайте и теперь имеете доступ к его полному функционалу',
            from_email="piton-kharitonov@yandex.ru",
            recipient_list=[receiver_email]
        )
        return super().form_valid(form)

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('catalog:index')
    login_url = reverse_lazy('users:register')





