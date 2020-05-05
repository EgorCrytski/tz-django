from django.urls import path
from . import views

app_name = 'library'
urlpatterns = [
    path('', views.index, name='index'),
    path('user/<int:user_id>/', views.user_books, name='user_books'),
    path('user/add/', views.add_user, name='add_user'),
    path('book/<int:book_id>/', views.book, name='book'),
    path('book/add/', views.add_book, name='add_book'),
    path('book/<int:book_id>/change/', views.change_book, name='change_book'),
    path('book/<int:book_id>/delete/', views.delete_book, name='delete_book'),
]
