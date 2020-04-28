from  rest_framework import serializers
from .models import User, Book

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= '__all__'


class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields= '__all__'