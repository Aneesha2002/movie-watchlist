import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from .models import Movie, UserMovie
from .serializers import MovieSerializer, UserMovieSerializer


TMDB_API_KEY = "YOUR_KEY_HERE"


@api_view(["GET"])
def search_movies(request):
    query = request.GET.get("q")
    if not query:
        return Response({"error": "Missing search query"}, status=400)

    url = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={query}"
    r = requests.get(url).json()
    return Response(r)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_to_watchlist(request):
    tmdb_id = request.data.get("tmdb_id")

    movie, created = Movie.objects.get_or_create(
        tmdb_id=tmdb_id,
        defaults={
            "title": request.data.get("title"),
            "poster_url": request.data.get("poster"),
            "overview": request.data.get("overview"),
            "genres": ",".join(request.data.get("genres", [])),
            "release_date": request.data.get("release_date"),
        }
    )

    user_movie, _ = UserMovie.objects.get_or_create(
        user=request.user,
        movie=movie
    )

    serializer = UserMovieSerializer(user_movie)
    return Response(serializer.data)
