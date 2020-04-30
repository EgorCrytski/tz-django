from django.db import models


class User(models.Model):
    user_name = models.CharField('User name', max_length=100)

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Book(models.Model):
    book_name = models.CharField('Book name', max_length=100)
    book_author = models.CharField('Book author', max_length=100)
    book_year = models.DateTimeField('Publishing date')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return self.book_name

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
