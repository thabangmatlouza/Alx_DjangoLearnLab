from django.db import models

class Library(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, default="unknown")

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    library = models.ForeignKey(Library, on_delete=models.CASCADE, related_name="books", default=1)
    publication_date = models.DateField(null=True, blank=True, default='2025-01-01')

    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
            ("can_publish_book", "Can publish book"),
            ("can_edit_book", "Can edit book"),
        ]

        ordering = ['title']

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    ROLE_ADMIN = "admin"
    ROLE_LIBRARIAN = "librarian"
    ROLE_MEMBER = "member"

    ROLE_CHOICES = [
        (ROLE_ADMIN, "Admin"),
        (ROLE_LIBRARIAN, "Librarian"),
        (ROLE_MEMBER, "Member"),
    ]

    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=ROLE_MEMBER)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

