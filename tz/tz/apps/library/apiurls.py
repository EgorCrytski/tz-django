from django.urls import path
from . import apiviews

app_name = 'library'
urlpatterns = [
    path('user/add/', apiviews.UserCreateView.as_view(), name='user_add'),
    path('user/detail/<int:pk>/', apiviews.UserDetailView.as_view(), name='user_detail'),
    path('user/all/', apiviews.UserListView.as_view(), name='user_list'),
    path('book/add', apiviews.BookCreateView.as_view(), name='book_add'),
    path('book/detail/<int:pk>/', apiviews.BookDetailView.as_view(), name='book_detail'),
    path('book/all/', apiviews.BookListView.as_view(), name='book_list'),
]
