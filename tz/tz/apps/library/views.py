from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Book, User

def index(request):
    users_list = User.objects.order_by('user_name')
    return render(request, 'library/list.html', {'users_list': users_list})

def user_books(request, user_id):
    try:
        user = User.objects.get( id = user_id )
        books = user.books.all()
    except:
        raise Http404("User not found")

    return render(request, 'library/userbooks.html', {'books', books}, {'user', user})

def add(request):
    a = User(user_name = request.POST['name'])
    a.save()
    return HttpResponseRedirect(reverse('library:index'))

def book(request, book_id):
    a = Book.objects.get(id = book_id)
    pass
