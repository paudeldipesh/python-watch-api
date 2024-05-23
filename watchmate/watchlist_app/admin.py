from django.contrib import admin
from watchlist_app.models import Review, StreamPlatform, WatchList

admin.site.register(WatchList)
admin.site.register(StreamPlatform)
admin.site.register(Review)
