from django.core.validators import FileExtensionValidator
from django.db import models


# Create your models here.
class Product(models.Model):
    """Модель с базовыми настройками продуктов"""

    name = models.CharField(
        max_length=150, verbose_name="наименование", help_text="Введите наименование"
    )
    description = models.TextField(
        verbose_name="описание", help_text="Введите описание", blank=True, null=True
    )
    image = models.ImageField(
        verbose_name="изображение",
        help_text="Выберете изображение",
        upload_to="catalog/img",
        blank=True,
        null=True,
        validators=[FileExtensionValidator(['jpeg'])]
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        verbose_name="категория",
        help_text="Выберете категорию",
        blank=True,
        null=True,
    )
    price = models.IntegerField(
        verbose_name="цена за покупку", help_text="Введите цену", blank=True, null=True
    )
    created_at = models.DateField(
        verbose_name="дата создания",
        help_text="Введите дату создания",
        blank=True,
        null=True,
    )
    updated_at = models.DateField(
        verbose_name="дата последнего изменения",
        help_text="Введите дату последнего обновления",
        blank=True,
        null=True,
    )

    def __str__(self):
        """Волшебный метод отвечающий за вывод информации на печать"""
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = [
            "name",
            "price",
        ]


class Category(models.Model):
    """Модель с базовыми настройками категорий"""

    name = models.CharField(
        max_length=150, verbose_name="наименование", help_text="Введите наименование"
    )
    description = models.TextField(
        verbose_name="описание", help_text="Введите описание", blank=True, null=True
    )

    def __str__(self):
        """Волшебный метод отвечающий за вывод информации на печать"""

        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = [
            "name",
        ]
