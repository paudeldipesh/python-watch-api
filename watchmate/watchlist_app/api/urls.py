from django.urls import path
from watchlist_app.api.views import WatchListAV, WatchDetailAV, StreamPlatformAV, StreamDetailAV

app_name = 'watchlist'

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='watch-list'),
    path('list/<int:pk>', WatchDetailAV.as_view(), name='watch-detail'),
    path('stream/', StreamPlatformAV.as_view(), name='stream-platform'),
    path('stream/<int:pk>', StreamDetailAV.as_view(), name='stream-detail'),
]
