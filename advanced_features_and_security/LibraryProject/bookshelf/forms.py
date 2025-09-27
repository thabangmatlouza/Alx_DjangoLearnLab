from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']  # ✅ fixed typo

class BookSearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, label='Search Books')

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
