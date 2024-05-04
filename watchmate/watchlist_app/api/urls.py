from django.urls import path
from watchlist_app.api.views import (
    ReviewCreate,
    ReviewDetail,
    ReviewList,
    StreamDetailAV,
    StreamPlatformAV,
    WatchDetailAV,
    WatchListAV,
)

urlpatterns = [
    path("list/", WatchListAV.as_view(), name="watch-list"),
    path("<int:pk>/", WatchDetailAV.as_view(), name="watch-detail"),
    path("stream/", StreamPlatformAV.as_view(), name="stream-list"),
    path("stream/<int:pk>/", StreamDetailAV.as_view(), name="streamplatform-detail"),
    path(
        "stream/<int:pk>/review-create/", ReviewCreate.as_view(), name="review-create"
    ),
    path("stream/<int:pk>/review/", ReviewList.as_view(), name="review-list"),
    path("stream/review/<int:pk>/", ReviewDetail.as_view(), name="review-detail"),
]
