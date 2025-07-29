import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from dotenv import load_dotenv

from .models import Publication

load_dotenv(override=True)


class BlogListView(ListView):
    model = Publication

    def get_queryset(self):
        return Publication.objects.filter(is_publicated=True)


class BlogDetailView(DetailView):
    model = Publication

    def send_simple_email(
        self,
        sender_email,
        receiver_email,
        subject,
        body,
        smtp_server,
        smtp_port,
        login,
        password,
    ):
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_shows += 1
        if self.object.number_shows == 100:
            sender_email = os.getenv("SENDER_EMAIL")
            receiver_email = os.getenv("RECEIVER_EMAIL")
            smtp_server = os.getenv("SMTP_SERVER")
            smtp_port = os.getenv("SMPT_PORT")
            login = os.getenv("LOGIN_SENDER")
            password = os.getenv("PASSWORD_SENDER")

            self.send_simple_email(
                sender_email,
                receiver_email,
                "Уведомление о достижении 100 просмотров",
                f"{self.object.title} достигла 100 просмотров, подзравляю!",
                smtp_server,
                smtp_port,
                login,
                password,
            )

        self.object.save()
        return self.object


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Publication
    fields = (
        "title",
        "content",
        "preview",
        "create_data",
        "is_publicated",
        "number_shows",
    )
    success_url = reverse_lazy("blog:blog_list")
    login_url = reverse_lazy("users:register")


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Publication
    fields = (
        "title",
        "content",
        "preview",
        "create_data",
        "is_publicated",
        "number_shows",
    )
    success_url = reverse_lazy("blog:blog_list")
    login_url = reverse_lazy("users:register")

    def get_success_url(self):
        return reverse("blog:blog_detail", args=[self.kwargs.get("pk")])


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Publication
    success_url = reverse_lazy("blog:blog_list")
    login_url = reverse_lazy("users:register")
