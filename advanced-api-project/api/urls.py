from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookUpdateView, BookDeleteView
from .views import BookList, BookViewSet (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

urlpatterns = [
    path('', include(router.urls)),
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),
]

