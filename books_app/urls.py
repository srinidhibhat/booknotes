from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
    UserBookListView
)
from . import views

urlpatterns = [
    path('', BookListView.as_view(), name = 'books_app-home'),
    path('user/<str:username>/', UserBookListView.as_view(), name = 'books_app-user_books'),
    # the below url is book specific i.e. after 'book/' primary key of the book takes us to specific book detail page
    path('book/<int:pk>/', BookDetailView.as_view(), name = 'books_app-detail'),
    path('book/new', BookCreateView.as_view(), name = 'books_app-create'),
    path('book/<int:pk>/update', BookUpdateView.as_view(), name = 'books_app-update'),
    path('book/<int:pk>/delete', BookDeleteView.as_view(), name = 'books_app-delete'),
    path('about/', views.about, name = 'books_app-about'),
]
