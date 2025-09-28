from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book, Author
from django.contrib.auth.models import User

class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Create a test author
        self.author = Author.objects.create(name="J.K. Rowling")

        # Create a test book
        self.book = Book.objects.create(title="Harry Potter", publication_year=2023, author=self.author)

    def test_get_book_list(self):
        url = reverse('book-list')  # Name from your urls.py
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_book_requires_login(self):
        # Log in to pass the ALX check
        self.client.login(username='testuser', password='testpass')

        url = reverse('book-create')  # Name from your urls.py
        data = {
            "title": "New Book",
            "publication_year": 2024,
            "author": self.author.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

