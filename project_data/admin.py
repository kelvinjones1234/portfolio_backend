from django.contrib import admin

from .models import CompletedProject, Credits


class CompleteProjectAdmin(admin.ModelAdmin):
    list_display = [
        "project_title",
    ]


admin.site.register(CompletedProject, CompleteProjectAdmin)
admin.site.register(Credits)
