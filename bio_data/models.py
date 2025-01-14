from django.db import models
from tinymce.models import HTMLField


class BioData(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    tel = models.CharField(max_length=15)
    address = models.CharField(max_length=300)
    about = HTMLField()
    experience = models.CharField(max_length=5)
    profile_pic = models.ImageField(upload_to="", null=True, blank=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Pesonal Information"
        verbose_name_plural = "Biographical Data"


class Stack(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class TechnicalExpertise(models.Model):
    stack = models.ForeignKey(
        Stack, related_name="technical_expertise", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Techinical Expertise"


class Socials(models.Model):
    social_media = models.CharField(max_length=50)
    link = models.CharField(max_length=100)

    def __str__(self):
        return self.social_media

    class Meta:
        verbose_name_plural = "Socials"
