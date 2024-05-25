from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Book, Author, Publisher
from .forms import BookForm, AuthorForm, PublisherForm

class BookListView(ListView):
    model = Book
    template_name = 'library/book_list.html'
    context_object_name = 'books'

class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'library/book_form.html'
    success_url = reverse_lazy('book-list')

class AuthorListView(ListView):
    model = Author
    template_name = 'library/author_list.html'
    context_object_name = 'authors'

class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'library/author_form.html'
    success_url = reverse_lazy('author-list')

class PublisherListView(ListView):
    model = Publisher
    template_name = 'library/publisher_list.html'
    context_object_name = 'publishers'

class PublisherCreateView(CreateView):
    model = Publisher
    form_class = PublisherForm
    template_name = 'library/publisher_form.html'
    success_url = reverse_lazy('publisher-list')

class PublishedBooksListView(ListView):
    model = Book
    template_name = 'library/published_books_list.html'
    context_object_name = 'books'
