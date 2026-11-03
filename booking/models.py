from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Назва категорії")
    description = models.TextField(blank=True, verbose_name="Опис категорії")

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=150, verbose_name="Назва страви")
    description = models.TextField(blank=True, verbose_name="Опис страви")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Ціна")
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='dishes',
        verbose_name="Категорія"
    )
    is_available = models.BooleanField(default=True, verbose_name="Доступність")

    class Meta:
        verbose_name = "Страва"
        verbose_name_plural = "Страви"

    def __str__(self):
        return f"{self.name} ({self.price} грн)"