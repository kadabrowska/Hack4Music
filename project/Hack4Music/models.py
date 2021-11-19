from django.db import models


class Release(models.Model):
    name = models.CharField(max_length=120)
    artist_name = models.CharField(max_length=120)
    released_date = models.DateField()
    image = models.URLField()



