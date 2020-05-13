from rest_framework import serializers
from .models import Book
from django.contrib.auth.models import User

class UserEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username",)


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username",)


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        exclude = ("id", "user",)


class BookCreateSerializer(serializers.ModelSerializer):


    class Meta:
        model = Book
        exclude = ("id",)


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class UserDetailSerializer(serializers.ModelSerializer):
    books = BookDetailSerializer(many=True)

    class Meta:
        model = User
        fields = '__all__'
