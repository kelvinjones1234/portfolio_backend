from rest_framework import serializers
from .models import Credits


class CreditsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credits
        fields = "__all__"
