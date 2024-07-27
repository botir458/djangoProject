from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, Model, ForeignKey, CASCADE, DateTimeField, TextChoices, SlugField, ImageField, \
    FloatField
from django.db.models.functions import Now
from django.utils.text import slugify


class SlugBase(Model):
    name = CharField(max_length=255)
    slug = CharField(max_length=255, unique=True, editable=False)

    class Meta:
        abstract = True

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        while self.__class__.objects.filter(slug=self.slug).exists():
            self.slug += '-1'
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.name

class CreatedBaseModel(Model):
    updated_at = DateTimeField(auto_now_add=True)
    created_at = DateTimeField(auto_now=True)


    class Meta:
        abstract = True


