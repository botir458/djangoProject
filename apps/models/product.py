from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, Model, ForeignKey, CASCADE, DateTimeField, TextChoices, SlugField, ImageField, \
    FloatField
from django.db.models.functions import Now
from apps.models.base import SlugBase



class Category(SlugBase):
    name = CharField(max_length=255)
    slug = SlugField(max_length=255, unique=True, editable=False)

    class Meta:
        verbose_name = 'kategorya'
        verbose_name_plural = 'kategoriyala'


class Product(SlugBase):
    name = CharField(max_length=255)
    price = FloatField(help_text="Product narxi uzb somda")
    category = ForeignKey('apps.Category', CASCADE)
    updated_at = DateTimeField(auto_now_add=True, db_default=Now())
    created_at = DateTimeField(auto_now_add=True, db_default=Now())
