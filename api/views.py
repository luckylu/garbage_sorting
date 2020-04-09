from api.models import Garbage
from rest_framework import status
from rest_framework.decorators import api_view
from api.serializers import GarbageSerializer, GarbageFuzzySearchSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
import logging as log

@api_view(['GET'])
def garbages(request, garbage):
    result = Garbage.objects.filter(name__contains = garbage)
    serializer = GarbageFuzzySearchSerializer(result, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def exact_garbages(request, garbage):
    log.info("搜索垃圾名："+garbage)
    result = Garbage.objects.filter(name = garbage)
    serializer = GarbageSerializer(result, many=True)
    return Response(serializer.data)
