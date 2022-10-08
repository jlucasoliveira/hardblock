from django.contrib import admin

from units import models


@admin.register(models.Unit)
class UnitAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("name", "description",)


@admin.register(models.Counter)
class CounterAdmin(admin.ModelAdmin):
    search_fields = ("name", "unit__name")
    list_filter = ("unit",)
    list_display = ("name", "description", "unit", "shared",)
    filter_horizontal = ("priorities",)


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    search_fields = ("name", "unit__name",)
    list_filter = ("unit",)
    list_display = ("name", "description", "busy", "shared", "unit",)


@admin.register(models.Address)
class AddressAdmin(admin.ModelAdmin):
    # Allow add and change on unit, but avoid edit directly
    def has_view_permission(self, *args, **kwargs) -> bool:
        return False
    
    def has_module_permission(self, *args, **kwargs) -> bool:
        return False
