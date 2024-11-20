from django.test import TestCase
from rest_framework.test import APIClient
from .models import CustomUser  # Import your model

# Create your tests here.
class YourTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword',
        }
        self.user = CustomUser.objects.create_user(**self.user_data)
        self.client.forcexite_authenticate(user=self.user)

def test_user_registration(self):
    response = self.client.post('/api/register/', self.user_data, format='json')
    self.assertEqual(response.status_code, 201)  # Assuming a successful registration returns HTTP 201

    
        
  
