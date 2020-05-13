from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    book_name = models.CharField('Book name', max_length=100)
    book_author = models.CharField('Book author', max_length=100)
    book_year = models.DateTimeField('Publishing date')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="books",)

    def __str__(self):
        return self.book_name

