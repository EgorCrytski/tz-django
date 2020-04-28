from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Book, User
from django.shortcuts import render
from rest_framework import generics
from .serializers import UserDetailSerializer, UserListSerializer, BookDetailSerializer, BookListSerializer


def index(request):
    users_list = User.objects.order_by('user_name')
    return render(request, 'library/list.html', {'users_list': users_list})


def user_books(request, user_id):
    try:
        user = User.objects.get(id = user_id)
        book_list = Book.objects.filter(user_id=user_id)
    except:
        raise Http404("User not found")

    return render(request, 'library/userbooks.html', {'books': book_list, 'user': user})


def book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except:
        raise Http404("Book not found")

    return render(request,'library/book.html', {'book': book})


def add_user(request):
    a = User(user_name=request.POST['name'])
    a.save()
    return HttpResponseRedirect(reverse('library:index'))


def add_book(request):
    user = User.objects.get(id=request.POST['userid'])
    a = Book(book_name=request.POST['book_name'], book_author = request.POST['book_author'],
             book_year = request.POST['book_year'], user_id = user)
    a.save()
    return HttpResponseRedirect(reverse('library:user_books', args = (user.id,)))


def change_book(request, book_id):
    book = Book(book_name=request.POST['book_name'], book_author = request.POST['book_author'],
                book_year = request.POST['book_year'], id = book_id)
    book.save()
    return HttpResponseRedirect(reverse('library:book', args = (book_id,)))


def delete_book(request, book_id):
    user = (Book.objects.get(id = book_id)).user_id
    Book.objects.filter(id = book_id).delete()
    return HttpResponseRedirect(reverse('library:user_books', args = (user.id,)))



class UserCreateView(generics.CreateAPIView):
    serializer_class = UserDetailSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()


class UserListView(generics.ListAPIView):
    serializer_class = UserListSerializer
    queryset = User.objects.all()


class BookCreateView(generics.CreateAPIView):
    serializer_class = BookDetailSerializer


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookDetailSerializer
    queryset = User.objects.all()


class BookListView(generics.ListAPIView):
    serializer_class = BookListSerializer
    queryset = User.objects.all()