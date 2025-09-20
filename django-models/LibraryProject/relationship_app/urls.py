from django.urls import path
from .views import list_books,LibraryDetailView,register_view
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # Books & Libraries
    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),

    # Authentication
    path("register/", register_view, name="register"),
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
]

