import json
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Book

def home(request):
    context = {
        'books': Book.objects.all(),
    }
    return render(request, 'books_app/home.html', context)

class BookListView(ListView):
    model = Book
    template_name = 'books_app/home.html'
    context_object_name = 'books'
    ordering = ['-date_added']
    # attribute to span out book list view into multiple pages (here 2 objects per page)
    paginate_by = 5

# view to list down books added by particular user
class UserBookListView(ListView):
    model = Book
    template_name = 'books_app/user_books.html'
    context_object_name = 'books'
    # attribute to span out book list view into multiple pages (here 2 objects per page)
    paginate_by = 5

    # get only those user objects which matches with selected 'added_by' attribute
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Book.objects.filter(added_by=user).order_by('-date_added')

class BookDetailView(DetailView):
    model = Book

# view to add in a Book through form
# inherit from LoginRequiredMixin for making login mandatory for adding a book
# also note that for fn based views we used decorators. here we just inherit from another built-in class
class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['name', 'author', 'notes']

    def form_valid(self, form):
        # automatically set the 'added by' attribute to current logged in user
        form.instance.added_by = self.request.user
        return super().form_valid(form)

# view to update the book details
class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Book
    fields = ['name', 'author', 'notes', 'pages', 'date_read']

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super().form_valid(form)

    # function to check whether the user trying to update the book details is the user who has created it
    # we don't want anybody to edit book details by any other user
    def test_func(self):
        # the book we are currently trying to update
        book = self.get_object()
        if self.request.user == book.added_by:
            return True
        return False

class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Book
    # url to redirect to after deleting
    success_url = '/'

    def test_func(self):
        # the book we are currently trying to update
        book = self.get_object()
        if self.request.user == book.added_by:
            return True
        return False

def about(request):
    return render(request, 'books_app/about.html')
