from rest_framework import serializers
from .models import Credits, CompletedProject


class CreditsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credits
        fields = "__all__"


class CompletedProjectSerializer(serializers.ModelSerializer):
    tech_used = (
        serializers.SerializerMethodField()
    )  # Custom field to return tech_used as text

    class Meta:
        model = CompletedProject
        fields = [
            "id",
            "project_title",
            "tech_used",
            "git_link",
            "project_link",
            "description",
            "image",
        ]

    def get_tech_used(self, obj):
        # Return a list of tech names as text
        return [tech.name for tech in obj.tech_used.all()]
