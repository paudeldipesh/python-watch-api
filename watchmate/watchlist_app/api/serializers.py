from rest_framework import serializers
from watchlist_app.models import Review, StreamPlatform, WatchList


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        exclude = ("watchlist",)


class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = WatchList
        fields = "__all__"


class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    watchlist = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="watch-detail"
    )

    class Meta:
        model = StreamPlatform
        fields = "__all__"
