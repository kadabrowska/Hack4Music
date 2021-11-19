from django.db import models


class Release(models.Model):
    name = models.CharField(max_length=120)
    artist_name = models.CharField(max_length=120)
    release_date = models.DateField()
    image = models.URLField()



