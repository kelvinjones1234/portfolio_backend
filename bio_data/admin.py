from django.contrib import admin
from .models import BioData, Stack, TechnicalExpertise, Socials


class BioDataAdmin(admin.ModelAdmin):

    list_display = ["full_name", "tel", "email"]


class StackAdmin(admin.ModelAdmin):

    list_display = [
        "name",
    ]


class TechnicalExpertiseAdmin(admin.ModelAdmin):
    list_display = ["name", "stack"]


class SocialsAdmin(admin.ModelAdmin):
    list_display = ["social_media", "link"]


admin.site.register(BioData, BioDataAdmin)
admin.site.register(Socials, SocialsAdmin)
admin.site.register(Stack)
admin.site.register(TechnicalExpertise, TechnicalExpertiseAdmin)
