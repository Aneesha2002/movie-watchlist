from django.urls import path
from . import views

urlpatterns = [
    path("search/", views.search_movies),
    path("watchlist/add/", views.add_to_watchlist),
]
