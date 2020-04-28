from django.urls import path
from . import views

app_name = 'library'
urlpatterns = [
    path('', views.index, name='index'),
    path('user/<int:user_id>/', views.user_books, name='user_books'),
    path('user/add/', views.add_user, name='add_user'),
    path('book/<int:book_id>/', views.book, name='book'),
    path('book/add/', views.add_book, name='add_book'),
    path('book/change/<int:book_id>', views.change_book, name='change_book'),
    path('book/delete/<int:book_id>', views.delete_book, name='delete_book'),
    path('api/user', views.UserCreateView.as_view()),
    path('api/user/detail/<int:pk>/', views.UserDetailView.as_view()),
    path('api/user/all', views.UserListView.as_view()),
    path('api/book', views.BookCreateView.as_view()),
    path('api/book/detail/<int:pk>/', views.BookDetailView.as_view()),
    path('api/book/all', views.BookListView.as_view()),

]
