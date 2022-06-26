from rest_framework import serializers
from .models import Animal
from characteristics.serializers import CharacteristicSerializer
from groups.serializers import GroupSerializer

class AnimalSerializer(serializers.Serializer):
    name = serializers.CharField()
    age = serializers.FloatField()
    weight = serializers.FloatField()
    sex = serializers.CharField()
    characteristics = CharacteristicSerializer(many=True)    
    group = GroupSerializer()
      
    def create(self, validated_data):
        return Animal.objects.create(**validated_data)
      
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
           
        instance.save()
        return instance