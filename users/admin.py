from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users import models

admin.AdminSite.site_header = "HardBlock"
admin.AdminSite.site_title = "HardBlock Admin"


@admin.register(models.User)
class UserAdmin(UserAdmin):
    fieldsets = (
        (
            "Informações Pessoais",
            {
                "fields": (
                    "name",
                    "email",
                    "password",
                    "phone_number",
                )
            },
        ),
        (
            "Permissões",
            {
                "fields": (
                    "is_staff",
                    "is_superuser",
                    "integration_code",
                    "units",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Datas Importantes", {"fields": ("last_login", "created_at")}),
    )
    readonly_fields = ("created_at",)
    list_display = (
        "username",
        "email",
        "name",
        "phone_number",
    )
    list_filter = (
        "is_staff",
        "is_superuser",
        "units",
    )
    filter_horizontal = (
        "user_permissions",
        "groups",
        "units",
    )
