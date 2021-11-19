from rest_framework import generics
from Hack4Music.serializers import ReleaseSerializer
from Hack4Music.models import Release


class ReleasesListView(generics.ListCreateAPIView):
    queryset = Release.objects.all()
    serializer_class = ReleaseSerializer
