from django.contrib.auth import login
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import UserRegisterForm
from users.models import User

from config.settings import EMAIL_HOST_USER

class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user=form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)


    def send_welcome_email(self, user_email):
        subject = 'Добро пожаловать!'
        message = 'Спасибо что присоединились  нашему сервису!'
        recipient_list = [user_email]
        from_email = EMAIL_HOST_USER
        send_mail(subject, message, from_email, recipient_list)
