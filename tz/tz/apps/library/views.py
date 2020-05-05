from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import Book, User
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserDetailSerializer, UserListSerializer, BookDetailSerializer, BookListSerializer, \
    BookCreateSerializer, UserCreateSerializer, UserEditSerializer, BookEditSerializer

def index(request):
    users_list = User.objects.order_by('user_name')
    return render(request, 'library/list.html', {'users_list': users_list})


def user_books(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        book_list = Book.objects.filter(user_id=user_id)
    except:
        raise Http404("User not found")

    return render(request, 'library/userbooks.html', {'books': book_list, 'user': user})


def book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except:
        raise Http404("Book not found")

    return render(request, 'library/book.html', {'book': book})


def add_user(request):
    a = User(user_name=request.POST['name'])
    a.save()
    return HttpResponseRedirect(reverse('library:index'))


def add_book(request):
    user = User.objects.get(id=request.POST['userid'])
    a = Book(book_name=request.POST['book_name'], book_author=request.POST['book_author'],
             book_year=request.POST['book_year'], user=user)
    a.save()
    return HttpResponseRedirect(reverse('library:user_books', args=(user.id,)))


def change_book(request, book_id):
    Book.objects.filter(id=book_id).update(book_name=request.POST['book_name'],
                                           book_author=request.POST['book_author'],
                                           book_year=request.POST['book_year'])

    return HttpResponseRedirect(reverse('library:book', args=(book_id,)))


def delete_book(request, book_id):
    user = (Book.objects.get(id=book_id)).user
    Book.objects.filter(id=book_id).delete()
    return HttpResponseRedirect(reverse('library:user_books', args=(user.id,)))





class user_list_view(APIView):
    serializer_class = UserListSerializer
    queryset = User.objects.all()

    def get(self, request):
        users = User.objects.all()
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data)


class user_detail_view(APIView):
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()

    def get(self, request, pk):
        user = User.objects.get(id=pk)
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)


class user_create_view(APIView):
    def post(self, request):
        user = UserCreateSerializer(data=request.data)
        if user.is_valid():
            user.save()
            return Response(status=201)
        else:
            return Response(status=400)


class user_edit_view(APIView):
    def put(self, request, pk):
        user = User.objects.get(id=pk)
        serializer = UserEditSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=202)
        else:
            return Response(status=400)


class user_delete_view(APIView):
    def post(self, request, pk):
        user = User.objects.get(id=pk)
        user.delete()
        return Response(status=202)


class book_list_view(APIView):
    serializer_class = BookListSerializer
    queryset = Book.objects.all()

    def get(self, request):
        books = Book.objects.all()
        serializer = BookListSerializer(books, many=True)
        return Response(serializer.data)


class book_detail_view(APIView):
    serializer_class = BookDetailSerializer
    queryset = Book.objects.all()

    def get(self, request, pk):
        book = Book.objects.get(id=pk)
        serializer = BookDetailSerializer(book)
        return Response(serializer.data)


class book_create_view(APIView):
    def post(self, request):
        book = BookCreateSerializer(data=request.data)
        if book.is_valid():
            book.save()
            return Response(status=201)
        else:
            return Response(status=400)


class book_edit_view(APIView):
    def put(self, request, pk):
        book = Book.objects.get(id=pk)
        serializer = BookEditSerializer(book, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=202)
        else:
            return Response(status=400)


class book_delete_view(APIView):
    def post(self, request, pk):
        book = Book.objects.get(id=pk)
        book.delete()
        return Response(status=202)
