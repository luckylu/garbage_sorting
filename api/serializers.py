from api.models import Garbage, Category
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class GarbageSerializer(serializers.HyperlinkedModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Garbage
        fields = ('name', 'category')

class GarbageFuzzySearchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Garbage
        fields = ['name']
