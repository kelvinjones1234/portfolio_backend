from rest_framework import serializers
from .models import BioData, Socials, Stack, TechnicalExpertise


class BioDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = BioData
        fields = "__all__"


class StackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stack
        fields = "__all__"


class TechnicalExpertiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnicalExpertise
        fields = "__all__"


class SocialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Socials
        fields = "__all__"
