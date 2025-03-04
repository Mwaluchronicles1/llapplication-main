from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Language, Lesson
from accounts.models import CustomUser


class LessonTests(APITestCase):
    def setUp(self):
        self.admin_user = CustomUser.objects.create_superuser(
            email='admin@test.com',
            password='testpass123'
        )
        self.language = Language.objects.create(
            name='English',
            code='en',
            is_active=True
        )
        self.client.force_authenticate(user=self.admin_user)

    def test_create_lesson(self):
        url = reverse('lesson-list')
        data = {
            'title': 'Test Lesson',
            'language': self.language.id,
            'content': 'Test content',
            'difficulty_level': 'BEGINNER',
            'order': 1
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.count(), 1)
        self.assertEqual(Lesson.objects.get().title, 'Test Lesson')
