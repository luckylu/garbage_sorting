from api.models import Garbage
from rest_framework import status
from rest_framework.decorators import api_view
from api.serializers import GarbageSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def garbages(request, garbage):
    result = Garbage.objects.filter(name__contains = garbage)
    serializer = GarbageSerializer(result, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def exact_garbages(request, garbage):
    result = Garbage.objects.filter(name = garbage)
    serializer = GarbageSerializer(result, many=True)
    return Response(serializer.data)
