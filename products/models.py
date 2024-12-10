from django.db import models
from django.contrib.auth import get_user_model
from utils.model_abstracts import Model
from django_extensions.db.models import (
    TimeStampedModel,
    ActivatorModel,
    TitleSlugDescriptionModel
)


User = get_user_model()


def product_image_path(instance, filename):
    return f"product/images/{instance.title}/{filename}"


class Category(TimeStampedModel, Model):
    title = models.CharField(max_length=100, verbose_name='Название категории товаров')

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товаров'

    def __str__(self):
        return self.title


class Product(TimeStampedModel,
    ActivatorModel,
    TitleSlugDescriptionModel,
    Model
    ):
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    seller = models.ForeignKey(User, related_name="products", on_delete=models.CASCADE)
    image = models.ImageField(upload_to=product_image_path, blank=True)
    stock = models.IntegerField(default=1)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='product_list',
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title