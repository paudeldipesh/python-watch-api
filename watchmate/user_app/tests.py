from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase


class RegisterTestCase(APITestCase):
    def test_register(self):
        data = {
            "username": "testcase",
            "email": "testcase@gmail.com",
            "password": "testcase",
            "confirm_password": "testcase",
        }
        response = self.client.post(reverse("register"), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
