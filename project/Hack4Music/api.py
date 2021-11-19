from Hack4Music.models import Release
from rest_framework import viewsets, permissions
from Hack4Music.serializers import ReleaseSerializer


class ReleaseViewSet(viewsets.ModelViewSet):
    queryset = Release.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ReleaseSerializer