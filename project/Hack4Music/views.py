from rest_framework import generics
from Hack4Music.serializers import ReleaseSerializer, ArticleSerializer, VideoSerializer, PodcastSerializer
from Hack4Music.models import Release, Article, Video, Podcast


class ReleasesListView(generics.ListCreateAPIView):
    queryset = Release.objects.all()
    serializer_class = ReleaseSerializer


class ArticleListView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class VideoListView(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class PodcastListView(generics.ListCreateAPIView):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer

