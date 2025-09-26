from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Home page
def home(request):
    return render(request, 'bookshelf/home.html')

# Book-related views
def list_books(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/list_books.html', {'books': books})

def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookshelf/edit_book.html', {'form': form, 'book': book})

# Library detail
def library_detail(request, pk):
    # Placeholder: replace with your Library model logic
    return render(request, 'bookshelf/library_detail.html', {'pk': pk})

# Authentication views
def register(request):
    # Placeholder for registration logic
    return render(request, 'bookshelf/register.html')

def login_view(request):
    # Placeholder for login logic
    return render(request, 'bookshelf/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

# Role-based views
@login_required
def admin_view(request):
    return render(request, 'bookshelf/admin_view.html')

@login_required
def librarian_view(request):
    return render(request, 'bookshelf/librarian_view.html')

@login_required
def member_view(request):
    return render(request, 'bookshelf/member_view.html')

