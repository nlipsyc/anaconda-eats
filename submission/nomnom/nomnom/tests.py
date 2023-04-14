from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
# Create your tests here.

class RecipeTests(APITestCase):
    def test_create_recipe(self):
        url = reverse('recipe-list')
        data = {
            "title": "Grilled Cheese",

            "instructions": "Put cheese between bread\r\nGrill on first side\r\nGrill on second side",
            "thumbnail": "http://www.sammich.com/grilledcheese.jpg",
            "cook_time": "00:01:00",
            "prep_time": "00:00:30",
            "total_time": "00:01:30",
            "serving_size": "1 sammich"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)