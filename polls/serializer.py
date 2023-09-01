from rest_framework import serializers
from .models import stakan, eshik


class stakanSerializer(serializers.ModelSerializer):
    class Meta:
        model=stakan
        fields = ('name', 'hajmi')


class eshikSerializer(serializers.ModelSerializer):
    class Meta:
        model=eshik
        fields=('nomi', 'boyi')



