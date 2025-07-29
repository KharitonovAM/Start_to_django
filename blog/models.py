from django.db import models


# Create your models here.
class Publication(models.Model):
    title = models.CharField(
        max_length=100, verbose_name="Заголовок", help_text="Укажите заголовок"
    )
    content = models.TextField(
        verbose_name="Содержание", help_text="Введите содержание статьи"
    )
    preview = models.ImageField(
        verbose_name="Preview",
        help_text="Выберете изображение для превью",
        upload_to="blog/img",
        null=True,
        blank=True,
    )
    create_data = models.DateField(
        verbose_name="дата создания",
        help_text="Введите дату создания",
        blank=True,
        null=True,
    )
    is_publicated = models.BooleanField(
        verbose_name="Признак пуликации",
        help_text="Укажите, опубликована статья ии нет",
        default=True,
    )
    number_shows = models.IntegerField(verbose_name="Количество просмотров", default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "блог"
        verbose_name_plural = "книги"
        ordering = ["title"]
