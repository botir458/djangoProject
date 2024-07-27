from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, Model, ForeignKey, CASCADE, DateTimeField, TextChoices, SlugField, ImageField, \
    FloatField
from django.db.models.fields import DateField
from django.db.models.functions import Now


class User(AbstractUser):
    class Type(TextChoices):
        ADMIN = 'admin', 'Admin'
        MODERATOR = 'moderator', 'Admin'
        TEACHER = 'job', 'Job'
        STUDENT = 'student', 'Student'

    class Gender(TextChoices):
        MALE = 'male', 'Male'
        FEMALE = 'female', 'Female'

    phone = CharField(max_length=25, blank=True, null=True)
    type = CharField(max_length=15, choices=Type.choices, db_default=Type.STUDENT)
    image = ImageField(upload_to='users/%Y/%m/%d/', default='users/default-avatar.jpg')
    gender = CharField(max_length=15 , default=Gender.MALE)
    birth_date = DateField(blank=True, null=True)

