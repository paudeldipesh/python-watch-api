from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from watchlist_app import models


class StreamPlatformTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="dipeshpaudel", password="Myself5862"
        )
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

        self.stream = models.StreamPlatform.objects.create(
            name="Test Case",
            about="About Test Case",
            website="https://www.testcase.com",
        )

    def test_streamplatform_create(self):
        data = {
            "name": "Test Case",
            "about": "About Test Case.",
            "website": "https://www.testcase.com",
        }
        response = self.client.post(reverse("streamplatform-list"), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_streamplatform_get(self):
        response = self.client.get(reverse("streamplatform-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_streamplatform_individual(self):
        response = self.client.get(
            reverse("streamplatform-detail", args=(self.stream.id,))
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class WatchListTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="dipeshpaudel", password="Myself5862"
        )
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

        self.stream = models.StreamPlatform.objects.create(
            name="Test Case",
            about="About Test Case",
            website="https://www.testcase.com",
        )
        self.watchlist = models.WatchList.objects.create(
            platform=self.stream,
            title="Movie Name",
            storyline="Movie Storyline",
            active=False,
        )

    def test_watchlist_create(self):
        data = {
            "platform": self.stream,
            "title": "Watch Name",
            "storyline": "Watch Storyline",
            "active": True,
        }

        response = self.client.post(reverse("watch-list"), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_watchlist_list(self):
        response = self.client.get(reverse("watch-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_watchlist_individual(self):
        response = self.client.get(reverse("watch-detail", args=(self.watchlist.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.WatchList.objects.count(), 1)
        self.assertEqual(models.WatchList.objects.get().title, "Movie Name")


class ReviewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testuser")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

        self.stream = models.StreamPlatform.objects.create(
            name="Test Stream",
            about="About Test Stream",
            website="https://www.testuser.com",
        )
        self.watchlist = models.WatchList.objects.create(
            platform=self.stream,
            title="Movie Name One",
            storyline="Movie Storyline One",
            active=False,
        )
        self.watchlist_two = models.WatchList.objects.create(
            platform=self.stream,
            title="Movie Name Two",
            storyline="Movie Storyline Two",
            active=False,
        )
        self.review = models.Review.objects.create(
            review_user=self.user,
            rating=5,
            description="Manual Description",
            watchlist=self.watchlist_two,
            active=True,
        )

    def test_review_create(self):
        data = {
            "review_user": self.user,
            "rating": 3,
            "description": "Test Review",
            "watchlist": self.watchlist,
            "active": True,
        }

        response = self.client.post(
            reverse("review-create", args=(self.watchlist.id,)), data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Review.objects.count(), 2)

        # Again creating a review
        response = self.client.post(
            reverse("review-create", args=(self.watchlist.id,)), data
        )
        self.assertEqual(response.status_code, status.HTTP_429_TOO_MANY_REQUESTS)

    def test_review_update(self):
        data = {
            "review_user": self.user,
            "rating": 4,
            "description": "Great Movie - Updated",
            "watchlist": self.watchlist,
            "active": False,
        }

        response = self.client.put(
            reverse("review-detail", args=(self.review.id,)), data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_review_list(self):
        response = self.client.get(reverse("review-list", args=(self.watchlist.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_review_individual(self):
        response = self.client.get(reverse("review-detail", args=(self.review.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_review_individual_delete(self):
        response = self.client.delete(reverse("review-detail", args=(self.review.id,)))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_review_user(self):
        response = self.client.get(f"/watch/reviews/?username={self.user.username}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
