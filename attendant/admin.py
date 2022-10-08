from django.contrib import admin

from attendant import models


@admin.register(models.Priority)
class PriorityAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "abbreviation", "personalized_service", "units_summary")
    filter_horizontal = ("units",)
