from relationship_app.models import Author, Book, Library, Librarian

# --- Create sample data if it doesn't exist ---
author, created = Author.objects.get_or_create(name="John Doe")
book, created = Book.objects.get_or_create(title="Python Basics", author=author)
library, created = Library.objects.get_or_create(name="City Library")
library.books.add(book)
librarian, created = Librarian.objects.get_or_create(name="Jane Smith", library=library)

# --- Queries ---

# 1. Query all books by a specific author
print("Books by John Doe:", list(Book.objects.filter(author=author)))

# 2. List all books in a library
library_name = "City Library"
library = Library.objects.get(name=library_name)
print(f"Books in {library_name}:", list(library.books.all()))

# 3. Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
print(f"Librarian for {library_name}:", librarian)

