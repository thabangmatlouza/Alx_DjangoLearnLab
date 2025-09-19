
---

### **`retrieve.md`**

```markdown
# Retrieve Book

```python
from bookshelf.models import Book

# Retrieve all books
books = Book.objects.all()
books
# Output: <QuerySet [<Book: 1984>]>

