from django.core.validators import MinValueValidator
from django.db import models


class Cart(models.Model):
    product = models.ForeignKey(
        'webapp.Product',
        related_name='products',
        on_delete=models.CASCADE,
        verbose_name='Продукт'
    )
    balance = models.IntegerField(
        null=False,
        blank=False,
        verbose_name="Количество",
        validators=[MinValueValidator(0)],
        default=None,
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Время создания"
    )

    def __str__(self):
        return f"{self.product} - {self.balance} - {self.product.price * self.balance}"

    class Meta:
        verbose_name = "Козрзина"
        verbose_name_plural = "Корзина"
        ordering = ["-created_at"]

