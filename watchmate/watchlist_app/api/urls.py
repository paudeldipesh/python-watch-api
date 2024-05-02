from django.urls import path
from watchlist_app.api.views import (
    StreamDetailAV,
    StreamPlatformAV,
    WatchDetailAV,
    WatchListAV,
)

urlpatterns = [
    path("list/", WatchListAV.as_view(), name="watch-list"),
    path("<int:pk>", WatchDetailAV.as_view(), name="watch-detail"),
    path("stream/", StreamPlatformAV.as_view(), name="stream-list"),
    path("stream/<int:pk>", StreamDetailAV.as_view(), name="stream-detail"),
]
