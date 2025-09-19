from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author = Author.objects.get(name="George Orwell")
books_by_author = Book.objects.filter(author=author)
print("Books by George Orwell:", list(books_by_author))

# List all books in a library
library = Library.objects.get(name="City Library")
books_in_library = library.books.all()
print("Books in City Library:", list(books_in_library))

# Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
print("Librarian for City Library:", librarian.name)

