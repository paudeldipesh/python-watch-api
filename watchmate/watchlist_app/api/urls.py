from django.urls import include, path
from rest_framework.routers import DefaultRouter
from watchlist_app.api.views import (
    ReviewCreate,
    ReviewDetail,
    ReviewList,
    StreamPlatformVS,
    WatchDetailAV,
    WatchListAV,
)

router = DefaultRouter()
router.register(r"stream", StreamPlatformVS, basename="streamplatform")

urlpatterns = [
    path("list/", WatchListAV.as_view(), name="watch-list"),
    path("<int:pk>/", WatchDetailAV.as_view(), name="watch-detail"),
    path("", include(router.urls)),
    path(
        "stream/<int:pk>/review-create/", ReviewCreate.as_view(), name="review-create"
    ),
    path("stream/<int:pk>/review/", ReviewList.as_view(), name="review-list"),
    path("stream/review/<int:pk>/", ReviewDetail.as_view(), name="review-detail"),
]
