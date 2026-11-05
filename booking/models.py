from django.db import models
from django.contrib.auth.models import User


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


class Table(models.Model):
    number = models.IntegerField(unique=True, verbose_name="Номер столика")
    seats = models.IntegerField(verbose_name="Кількість місць")
    is_available = models.BooleanField(default=True, verbose_name="Доступність")

    class Meta:
        verbose_name = "Столик"
        verbose_name_plural = "Столики"

    def __str__(self):
        return f"Стіл №{self.number} (Місць: {self.seats})"


class Reservation(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Очікує'),
        ('confirmed', 'Підтверджено'),
        ('cancelled', 'Скасовано'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations', verbose_name="Користувач")
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='reservations', verbose_name="Столик")
    date = models.DateField(verbose_name="Дата бронювання")
    time = models.TimeField(verbose_name="Час бронювання")
    guests_count = models.IntegerField(verbose_name="Кількість гостей")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="Статус")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Бронювання"
        verbose_name_plural = "Бронювання"

    def __str__(self):
        return f"Бронь #{self.id} - Користувач: {self.user.username} (Стіл №{self.table.number})"