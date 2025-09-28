from django.db import models

class Author(models.Model):
    """
    Author model represents a writer who can have multiple books.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Book model represents a book written by an author.
    - Each book is linked to one Author.
    - publication_year must not be in the future (checked in serializer).
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
