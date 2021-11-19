from rest_framework import serializers
from Hack4Music.models import Release


class ReleaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Release
        fields = '__all__'