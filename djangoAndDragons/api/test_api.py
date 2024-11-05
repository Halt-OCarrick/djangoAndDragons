import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import *


# Create your tests here.
class TestCharacter(APITestCase):  # TODO: Add more tests to this class
    @pytest.mark.django_db
    def test_post_character(self):
        url = reverse('post_character')
        data = {
            "name": "Nariko Myastan",
            "level": 9,
            "init_bonus": 0,
            "armor_class": 18,
            "speed": "30 ft.",
            "passive_perception": 9,
            "is_concentrating": False,
            "max_hit_points": 67,
            "temp_hit_points": 0,
            "current_hit_points": 67,
            "campaign": [{"id": 1}]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    @pytest.mark.django_db
    def test_get_put_del_character(self):
        url = reverse('get_put_del_character', kwargs={"id": 1})
        response = self.client.get(url, format='json')
        print(response)
        # self.assertEqual(response.status_code, status.HTTP_200_OK)


"""
class TestCreature(APITestCase):
    def test_post_creature(self):
        url = reverse('post_creature')
        data = {
            "name": "Bandit Captain",
            "challenge_rating": 2,
            "init_bonus": 3
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_get_creatures(self):
        url = reverse('get_creatures')
        response = self.client.get(url, format='json')
        """