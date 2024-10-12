from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

class ClientTestCase(APITestCase):
    def test_create_client(self):
        url = reverse('client-create')
        data = {
            "location": "USA",
            "accountStatus": "Active"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], "Client created successfully!")
