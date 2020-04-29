from .models import Book, User
from rest_framework import generics
from .serializers import UserDetailSerializer, UserListSerializer, BookDetailSerializer, BookListSerializer


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
    queryset = Book.objects.all()


class BookListView(generics.ListAPIView):
    serializer_class = BookListSerializer
    queryset = Book.objects.all()
