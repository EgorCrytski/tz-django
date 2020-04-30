from django.urls import path
from . import apiviews

app_name = 'library'
urlpatterns = [
    path('user/add/', apiviews.UserCreateView.as_view(), name='user_add'),
    path('user/<int:pk>/', apiviews.UserDetailView.as_view(), name='user_detail'),
    path('user/<int:pk>/edit', apiviews.UserEditView.as_view(), name='user_edit'),
    path('user/all/', apiviews.UserListView.as_view(), name='user_list'),
    path('book/add/', apiviews.BookCreateView.as_view(), name='book_add'),
    path('book/<int:pk>/', apiviews.BookDetailView.as_view(), name='book_detail'),
    path('book/<int:pk>/edit', apiviews.BookCreateView.as_view(), name='book_edit'),
    path('book/all/', apiviews.BookListView.as_view(), name='book_list'),
]
