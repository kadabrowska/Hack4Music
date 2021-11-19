from django.db.migrations import serializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Hack4Music.serializers import ReleaseSerializer
from Hack4Music.models import Release
from django.http import HttpResponse, JsonResponse


def ReleasesListView(request, *args, **kwargs):
    per_page = request.GET.get('per_page')

    queryset = Release.objects.all().order_by('release_date')
    serializer_class = ReleaseSerializer

    serializer = serializer_class(queryset, many=True)
    return JsonResponse(serializer.data, safe=False)


