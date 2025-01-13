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
    stack = serializers.SerializerMethodField()  

    class Meta:
        model = TechnicalExpertise
        fields = ['id', 'name', 'stack']

    def get_stack(self, obj):
        # Return the stack name as text
        return obj.stack.name if obj.stack else None


class SocialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Socials
        fields = "__all__"
