from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User

from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from django.urls import reverse

class UserTestCase(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(username='testuser', password='12345')
        self.assertEqual(user.username, 'testuser')

    def test_update_user(self):
        user = User.objects.create_user(username='testuser', password='12345')
        user.username = 'updateduser'
        user.save()
        self.assertEqual(user.username, 'updateduser')

    def test_delete_user(self):
        user = User.objects.create_user(username='testuser', password='12345')
        user_id = user.id
        user.delete()
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(pk=user_id)

    def test_user_authentication(self):
        user = User.objects.create_user(username='testuser', password='12345')
        login = self.client.login(username='testuser', password='12345')
        self.assertTrue(login)