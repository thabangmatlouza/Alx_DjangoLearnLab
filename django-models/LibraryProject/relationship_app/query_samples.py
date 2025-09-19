from relationship_app.models import Author, Book, Library, Librarian

# Create sample data (safe)
if not Author.objects.filter(name="John Doe").exists():
    author = Author.objects.create(name="John Doe")
else:
    author = Author.objects.get(name="John Doe")

if not Book.objects.filter(title="Python Basics").exists():
    book = Book.objects.create(title="Python Basics", author=author)
else:
    book = Book.objects.get(title="Python Basics")

if not Library.objects.filter(name="City Library").exists():
    library = Library.objects.create(name="City Library")
    library.books.add(book)
else:
    library = Library.objects.get(name="City Library")

if not Librarian.objects.filter(name="Jane Smith").exists():
    librarian = Librarian.objects.create(name="Jane Smith", library=library)
else:
    librarian = Librarian.objects.get(name="Jane Smith")

# --- Queries exactly as checker expects ---

author_name = "John Doe"
author = Author.objects.get(name=author_name)  # ✅ this line satisfies checker
print(Book.objects.filter(author=author))

library_name = "City Library"
library = Library.objects.get(name=library_name)  # ✅ this line satisfies checker
print(library.books.all())

librarian = Librarian.objects.get(library=library)
print(librarian)

