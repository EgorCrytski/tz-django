from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import User, Book

class UserTests(APITestCase)
    def test_add_user(selfself):
        url = reverse('')

