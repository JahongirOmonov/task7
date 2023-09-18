from rest_framework import serializers
from .models import stakan, eshik
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User 


class stakanSerializer(serializers.ModelSerializer):
    class Meta:
        model=stakan
        fields = ('name', 'hajmi', 'user')

    def create(self, validated_data):
        validated_data['user']=get_object_or_404(User, username=self.context['request'].user)
        return super(stakanSerializer, self).create(validated_data)


class eshikSerializer(serializers.ModelSerializer):
    class Meta:
        model=eshik
        fields=('nomi', 'boyi', 'user')

    def create(self, validated_data):
        validated_data['user']=get_object_or_404(User, username=self.context['request'].user)
        return super(eshikSerializer, self).create(validated_data)



