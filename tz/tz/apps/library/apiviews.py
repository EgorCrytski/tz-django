from .models import Book, User
from rest_framework import generics
from .serializers import UserDetailSerializer, UserListSerializer, BookDetailSerializer, BookListSerializer


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserDetailSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserDetailSerializer
    lookup_field = 'pk'
    queryset = User.objects.all()


class UserListView(generics.ListAPIView):
    serializer_class = UserListSerializer
    queryset = User.objects.all()


class BookCreateView(generics.CreateAPIView):
    serializer_class = BookDetailSerializer


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookDetailSerializer
    lookup_field = 'pk'
    queryset = Book.objects.all()


class BookListView(generics.ListAPIView):
    serializer_class = BookListSerializer
    queryset = Book.objects.all()
