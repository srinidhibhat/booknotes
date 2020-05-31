from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Book(models.Model):
    name = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    notes = models.TextField(blank=True)
    date_added = models.DateTimeField(default=timezone.now)
    pages = models.IntegerField()
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    # this is to tell django how to find the url to any specific instance of the Book
    def get_absolute_url(self):
        # this allows us to redirect to book detail page after adding a new book (new instance)
        return reverse('books_app-detail', kwargs={'pk' : self.pk})
