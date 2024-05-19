from django.urls import include, path
from rest_framework.routers import DefaultRouter
from watchlist_app.api.views import (
    ReviewCreate,
    ReviewDetail,
    ReviewList,
    StreamPlatformVS,
    UserReview,
    WatchDetailAV,
    WatchListAV,
)

router = DefaultRouter()
router.register(r"stream", StreamPlatformVS, basename="streamplatform")

urlpatterns = [
    path("list/", WatchListAV.as_view(), name="watch-list"),
    path("<int:pk>/", WatchDetailAV.as_view(), name="watch-detail"),
    path("", include(router.urls)),
    path("<int:pk>/create-review/", ReviewCreate.as_view(), name="review-create"),
    path("<int:pk>/reviews/", ReviewList.as_view(), name="review-list"),
    path("review/<int:pk>/", ReviewDetail.as_view(), name="review-detail"),
    # path("reviews/<str:username>/", UserReview.as_view(), name="user-review-detail"),
    path("reviews/", UserReview.as_view(), name="user-review-detail"),
]
