from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import Book, Author
from django.contrib.auth.models import User


class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        # Create a test author
        self.author = Author.objects.create(name="J.K. Rowling")

        # Create a test book
        self.book = Book.objects.create(title="Harry Potter", publication_year=2000, author=self.author)

        def test_get_book_list(self):
        url = reverse('book-list')  # This is the name of your list view
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_create_book(self):
        url = reverse('book-list')
        data = {
            "title": "New Book",
            "publication_year": 2021,
            "author": self.author.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)

