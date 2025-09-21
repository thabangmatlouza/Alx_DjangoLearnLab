from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from .models import Library
from .models import Book
from .models import UserProfile
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

# Class-based view for library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})


@login_required
def logout_view(request):
    logout(request)
    return render(request, "relationship_app/logout.html")

def is_admin(user):
    try:
        return user.userprofile.role == UserProfile.ROLE_ADMIN
    except Exception:
        return False

def is_librarian(user):
    try:
        return user.userprofile.role == UserProfile.ROLE_LIBRARIAN
    except Exception:
        return False

def is_member(user):
    try:
        return user.userprofile.role == UserProfile.ROLE_MEMBER
    except Exception:
        return False

# --- Role-restricted views ---
@user_passes_test(is_admin, login_url='login')
@login_required
def admin_view(request):
    # put admin-only context/data here
    return render(request, "relationship_app/admin_view.html", {"user": request.user})

@user_passes_test(is_librarian, login_url='login')
@login_required
def librarian_view(request):
    # put librarian-only context/data here
    return render(request, "relationship_app/librarian_view.html", {"user": request.user})

@user_passes_test(is_member, login_url='login')
@login_required
def member_view(request):
    # put member-only context/data here
    return render(request, "relationship_app/member_view.html", {"user": request.user})
