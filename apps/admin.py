from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.models import Product, Category, StudentUser, TeacherUser
from django.utils.translation import gettext_lazy as _


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'price'
    autocomplete_fields = ['category']


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(StudentUser)
class StudentModelAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", "birth_date")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    def get_queryset(self, request):
        return super().get_queryset(request).filter(type=StudentUser.Type.STUDENT)


@admin.register(TeacherUser)
class TeacherModelAdmin(UserAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).filter(type=TeacherUser.Type.TEACHER)

# class CategoryModelAdmin(admin.ModelAdmin):
#      search_fields = ['name']
