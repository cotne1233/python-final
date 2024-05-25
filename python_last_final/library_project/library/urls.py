from django.urls import path
from .views import BookListView, BookCreateView, AuthorListView, AuthorCreateView, PublisherListView, PublisherCreateView, PublishedBooksListView

urlpatterns = [
    path('', PublishedBooksListView.as_view(), name='published-books-list'),
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/new/', BookCreateView.as_view(), name='book-create'),
    path('authors/', AuthorListView.as_view(), name='author-list'),
    path('authors/new/', AuthorCreateView.as_view(), name='author-create'),
    path('publishers/', PublisherListView.as_view(), name='publisher-list'),
    path('publishers/new/', PublisherCreateView.as_view(), name='publisher-create'),
]
