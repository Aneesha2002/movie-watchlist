from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    tmdb_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=255)
    poster_url = models.URLField(blank=True)
    overview = models.TextField(blank=True)
    release_date = models.CharField(max_length=20, blank=True)
    genres = models.CharField(max_length=255, blank=True)  # “Action, Sci-Fi”

    def __str__(self):
        return self.title


class UserMovie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    watched = models.BooleanField(default=False)
    rating = models.IntegerField(null=True, blank=True)  # 1–10
    notes = models.TextField(blank=True)

    class Meta:
        unique_together = ("user", "movie")

    def __str__(self):
        return f"{self.user.username} - {self.movie.title}"
