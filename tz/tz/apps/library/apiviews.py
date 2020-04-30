from .models import Book, User
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserDetailSerializer, UserListSerializer, BookDetailSerializer, BookListSerializer, \
    BookCreateSerializer, UserCreateSerializer, UserEditSerializer


class UserListView(APIView):
    serializer_class = UserListSerializer
    queryset = User.objects.all()

    def get(self, request):
        users = User.objects.all()
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data)


class UserDetailView(APIView):
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()

    def get(self, request, pk):
        user = User.objects.get(id=pk)
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)


class UserCreateView(APIView):
    def post(self, request):
        user = UserCreateSerializer(data=request.data)
        if user.is_valid():
            user.save()
        return Response(status=201)

class UserEditView(APIView):
    def put(self, request, pk):
        user = User.objects.get(id=pk)
        serializer = UserEditSerializer(user, data =request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status = 202)
        else:
            return Response(status=400)


class BookListView(APIView):
    serializer_class = BookListSerializer
    queryset = Book.objects.all()

    def get(self, request):
        books = Book.objects.all()
        serializer = BookListSerializer(books, many=True)
        return Response(serializer.data)


class BookDetailView(APIView):
    serializer_class = BookDetailSerializer
    queryset = Book.objects.all()

    def get(self, request, pk):
        book = Book.objects.get(id=pk)
        serializer = BookDetailSerializer(book)
        return Response(serializer.data)

class BookCreateView(APIView):
    def post(self, request):
        book = BookCreateSerializer(data=request.data)
        if book.is_valid():
            book.save()
        return Response(status=201)


"""
{
"book_name":"book1",
"book_author":"author1",
"book_year":"1212-12-21T00:00:00Z",
"user": 1
}
"""