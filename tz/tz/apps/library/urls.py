from django.urls import path
from . import views

app_name = 'library'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('user/<int:user_id>/', views.user_books, name = 'user_books'),
    path('user/add/', views.add, name = 'add'),
    path('book/<int:book_id>/', views.book, name = 'book')
]
