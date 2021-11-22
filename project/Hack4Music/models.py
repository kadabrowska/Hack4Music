from datetime import datetime

from django.db import models


class Release(models.Model):
    name = models.CharField(max_length=120)
    artist_name = models.CharField(max_length=120)
    release_date = models.DateField(default=datetime.now().strftime("%Y-%m-%d"))
    image = models.URLField()

    def __str__(self):
        return self.name


class Podcast(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    url = models.URLField()
    published_at = models.DateField(default=datetime.now().strftime("%Y-%m-%d"))
    tag_name = models.CharField(max_length=120)
    image = models.URLField()
    host_name = models.CharField(max_length=120)

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    content = models.TextField()
    tag_name = models.CharField(max_length=120)
    image = models.URLField()
    published_at = models.DateField(default=datetime.now().strftime("%Y-%m-%d"))

    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=120)
    url = models.URLField()
    description = models.CharField(max_length=1200)
    picture = models.URLField()
    author = models.CharField(max_length=120)
    tag_name = models.CharField(max_length=120)
    published_at = models.DateField(default=datetime.now().strftime("%Y-%m-%d"))

    def __str__(self):
        return self.title



