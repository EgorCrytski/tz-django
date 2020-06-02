from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from rest_framework import permissions
from .models import Book, User
from django.contrib.auth.models import User
from rest_framework.views import APIView
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
from rest_framework.response import Response
from .serializers import UserDetailSerializer, UserListSerializer, BookDetailSerializer, BookListSerializer, \
    BookCreateSerializer, UserCreateSerializer, UserEditSerializer, BookEditSerializer

class UserListView(APIView):
    serializer_class = UserListSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        users = User.objects.all()
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data)

    def get_serializer(self):
        return UserListSerializer()


class UserDetailView(APIView):
    '''Просмотр информации о пользователе'''
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()

    permission_classes = [permissions.IsAdminUser]

    def get(self, request, uid):
        user = get_object_or_404(User, id=uid)
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)


    def get_serializer(self):
        return UserDetailSerializer()


class SelfUserDetailView(APIView):
    '''Просмотр информации о текущем авторизованном пользователе'''
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = get_object_or_404(User, id = request.user.id)
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)


    def get_serializer(self):
        return UserDetailSerializer()


class UserCreateView(APIView):
    '''Создать нового пользователя'''
    permission_classes = [permissions.IsAdminUser]

    def post(self, request):
        user = UserCreateSerializer(data=request.data)
        if user.is_valid():
            user.save()
            return Response(status=201)
        else:
            return Response(status=400)

    def get_serializer(self):
        return UserCreateSerializer()


class UserEditView(APIView):
    '''Редактировать пользователя'''
    permission_classes = [permissions.IsAdminUser]

    def put(self, request, uid):
        user = get_object_or_404(User, id = uid)
        serializer = UserEditSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=200)
        else:
            return Response(status=400)

    def get_serializer(self):
        return UserEditSerializer()


class UserDeleteView(APIView):
    '''Удалить пользователя'''
    permission_classes = [permissions.IsAdminUser]

    def post(self, request, uid):
        user = get_object_or_404(User, id = uid)
        user.delete()
        return Response(status=200)



class BookListView(APIView):
    '''Список всех книг'''
    serializer_class = BookListSerializer
    queryset = Book.objects.all()
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        books = Book.objects.all()
        serializer = BookListSerializer(books, many=True)
        return Response(serializer.data)

    def get_serializer(self):
        return BookListSerializer()


class BookDetailView(APIView):
    '''Подробная информация о книге'''
    serializer_class = BookDetailSerializer
    queryset = Book.objects.all()
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, uid, bid):
        book = get_object_or_404(Book, user=uid, id = bid)
        serializer = BookDetailSerializer(book)
        return Response(serializer.data)

    def get_serializer(self):
        return BookDetailSerializer()


class BookCreateView(APIView):
    '''Создать новую книгу'''
    serializer_class = BookCreateSerializer
    permission_classes = [permissions.IsAdminUser]

    def post(self, request):

        book = BookCreateSerializer(data=request.data, )
        if book.is_valid():
            book.save()
            return Response(status=201)
        else:
            return Response(status=400)

    def get_serializer(self):
        return BookCreateSerializer()


class SelfBookCreateView(APIView):
    '''Создать новую книгу для текущего авторизованного пользователя'''
    serializer_class = BookCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        data = request.data.copy()
        print('\n\n\n\n\n\n\n\n')
        data['user'] = request.user.id
        print(request.data)
        print(data)
        print('\n\n\n\n\n\n\n\n')
        book = BookCreateSerializer(data=data, )
        if book.is_valid():
            book.save()
            return Response(status=201)
        else:
            return Response(status=400)

    def get_serializer(self):
        return BookCreateSerializer()


class BookEditView(APIView):
    permission_classes = [permissions.IsAdminUser]
    '''Редактировать книгу'''
    def put(self, request, uid, bid):
        book = Book.objects.filter(user=uid)
        book = book[bid - 1]
        serializer = BookEditSerializer(book, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=200)
        else:
            return Response(status=400)

    def get_serializer(self):
        return BookEditSerializer()


class BookDeleteView(APIView):
    '''Удалить книгу'''
    permission_classes = [permissions.IsAdminUser]

    def post(self, request, uid, bid):
        book = Book.objects.filter(user=uid)
        if book.count() > 0:
            book = book[bid - 1]
            book.delete()
            return Response(status=200)
        else:
            return Response(status=404)

