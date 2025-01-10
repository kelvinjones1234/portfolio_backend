from django.db import models
from bio_data.models import TechnicalExpertise
from tinymce.models import HTMLField


class Credits(models.Model):
    project_completed = models.CharField(max_length=7)
    happy_clients = models.CharField(max_length=7)
    success_rate = models.CharField(max_length=7)


    class Meta:
        verbose_name_plural = 'Credits'

class CompletedProject(models.Model):
    project_title = models.CharField(max_length=200)
    tech_used = models.ManyToManyField(TechnicalExpertise)
    git_link = models.CharField(max_length=1000)
    project_link = models.CharField(max_length=1000)
    description = HTMLField()

    def __str__(self):
        return self.project_title
    
    class Meta:
        verbose_name_plural = 'Completed Projects'