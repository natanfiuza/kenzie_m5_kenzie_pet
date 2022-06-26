from rest_framework import serializers
from .models import Group

class GroupSerializer(serializers.Serializer):
    name = serializers.CharField()
    scientific_name = serializers.CharField()
    
      
    def create(self, validated_data):
        return Group.objects.create(**validated_data)
      
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.scientific_name = validated_data.get('scientific_name', instance.scientific_name)
       
        instance.save()
        return instance