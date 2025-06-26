from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Publication
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv
import os

load_dotenv(override=True)

class BlogListView(ListView):
    model = Publication

    def get_queryset(self):
        return Publication.objects.filter(is_publicated=True)


class BlogDetailView(DetailView):
    model = Publication

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
        self.object.number_shows += 1
        if self.object.number_shows == 100:
            pass
            sender_email = os.getenv('SENDER_EMAIL')
            receiver_email = os.getenv('RECEIVER_EMAIL')
            smtp_server = os.getenv('SMTP_SERVER')
            smtp_port = os.getenv('SMPT_PORT')
            login = os.getenv('LOGIN_SENDER')
            password = os.getenv('PASSWORD_SENDER')

            self.send_simple_email(sender_email,
                                   receiver_email,
                                   "Уведомление о достижении 100 просмотров",
                                   f"{self.object.title} достигла 100 просмотров, подзравляю!",
                                   smtp_server,
                                   smtp_port,
                                   login,
                                   password)

        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    model = Publication
    fields = ("title", "content", "preview", "create_data", 'is_publicated', 'number_shows')
    success_url = reverse_lazy("blog:blog_list")


class BlogUpdateView(UpdateView):
    model = Publication
    fields = ('title', 'content', 'preview', 'create_data', 'is_publicated', 'number_shows')
    success_url = reverse_lazy('blog:blog_list')

    def get_success_url(self):
        return reverse('blog:blog_detail', args=[self.kwargs.get('pk')])

class BlogDeleteView(DeleteView):
    model = Publication
    success_url = reverse_lazy('blog:blog_list')