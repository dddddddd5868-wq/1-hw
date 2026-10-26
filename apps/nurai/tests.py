from django.test import TestCase

from .models import Student


class StudentIndexTest(TestCase):
    def test_homepage_displays_all_students(self):
        Student.objects.create(
            name='Анна Иванова',
            age=20,
            city='Бишкек',
            email='anna@example.com',
        )
        Student.objects.create(
            name='Иван Петров',
            age=22,
            city='Ош',
            email='ivan@example.com',
        )

        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, 'Анна Иванова — 20 лет, Бишкек')
        self.assertContains(response, 'Иван Петров — 22 лет, Ош')
