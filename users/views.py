import os
import secrets

from django.contrib.auth import login
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from users.forms import UserRegisterForm
from users.models import User

from config.settings import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_USER_TLS, EMAIL_USER_SSL, EMAIL_PORT, EMAIL_HOST

class UserCreateView(CreateView):


    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')



    def send_simple_email(self, sender_email, receiver_email, subject, body, smtp_server, smtp_port, login, password):
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        sender_email = EMAIL_HOST_USER
        receiver_email = self.object.email
        smtp_server = EMAIL_HOST
        smtp_port = EMAIL_PORT
        login = EMAIL_HOST_USER
        password = EMAIL_HOST_PASSWORD
        print('sdgsdfg')
        self.send_simple_email(sender_email,
                                receiver_email,
                                "Уведомление о регистрации",
                                   'Поздравляю. вы зарегистрировались у нас на сайте и теперь имеете доступ к его полному функционалу',
                                   smtp_server,
                                   smtp_port,
                                   login,
                                   password)

        self.object.save()
        return self.object
