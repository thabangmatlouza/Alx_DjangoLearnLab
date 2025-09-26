from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # Secured book views
    path("add_book/", views.add_book_view, name="add_book"),
    path("edit_book/<int:pk>/", views.edit_book_view, name="edit_book"),
    path("delete_book/<int:pk>/", views.delete_book_view, name="delete_book"),

    # Books & Libraries
    path("books/", views.list_books, name="list_books"),
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),

    # Authentication
    path("register/", views.register, name="register"),
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),

    # Role-based pages
    path("admin-view/", views.admin_view, name="admin_view"),
    path("librarian-view/", views.librarian_view, name="librarian_view"),
    path("member-view/", views.member_view, name="member_view"),
]

