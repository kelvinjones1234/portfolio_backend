from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import BioData, Stack, TechnicalExpertise, Socials
from project_data.models import Credits
from project_data.serializers import CreditsSerializer
from .serializers import (
    BioDataSerializer,
    StackSerializer,
    TechnicalExpertiseSerializer,
    SocialsSerializer,
)


class AllDataView(APIView):
    def get(self, request, *args, **kwargs):
        # Fetch all data
        biodata = BioData.objects.first()  
        stacks = Stack.objects.all()
        technical_expertise = TechnicalExpertise.objects.all()
        socials = Socials.objects.all()
        credits = Credits.objects.first() 

        # Serialize the data
        biodata_serializer = BioDataSerializer(biodata)
        stacks_serializer = StackSerializer(stacks, many=True)
        technical_expertise_serializer = TechnicalExpertiseSerializer(
            technical_expertise, many=True
        )
        socials_serializer = SocialsSerializer(socials, many=True)
        credits_serializer = CreditsSerializer(credits)

        # Combine all data into a single response
        response_data = {
            "biodata": biodata_serializer.data,
            "stacks": stacks_serializer.data,
            "technical_expertise": technical_expertise_serializer.data,
            "socials": socials_serializer.data,
            "credits": credits_serializer.data,
        }

        return Response(response_data, status=status.HTTP_200_OK)
