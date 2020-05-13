from django.contrib import admin

# Register your models here.
from .models import User, Book

#admin.site.unregister(User)
admin.site.register(Book)
