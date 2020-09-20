from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from markupfield.fields import MarkupField
from PIL import Image

class Book(models.Model):
    name = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    notes = MarkupField(default_markup_type='markdown', blank=True)
    date_added = models.DateTimeField(default=timezone.now)
    pages = models.IntegerField(null=True, blank=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_read = models.DateField(null=True, blank=True)
    # keeping it between 1-5
    rating = models.FloatField(
        null=True,
        blank=True,
        validators=[MaxValueValidator(5), MinValueValidator(1)]
        )
    # dropdown with two choices
    read_mode = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        choices=(('HardCopy', 'Hard Copy'),
                 ('ebook-PDF', 'eBook-PDF'),
                 ('ebook-Kindle', 'eBook-Kindle'))
        )
    time_taken = models.FloatField(null=True, blank=True)


    def __str__(self):
        return self.name

    # this is to tell django how to find the url to any specific instance of the Book
    def get_absolute_url(self):
        # this allows us to redirect to book detail page after adding a new book (new instance)
        return reverse('books_app-detail', kwargs={'pk' : self.pk})
