from django.urls import path
from . import views

app_name = 'library'
urlpatterns = [
    path('', views.index, name='index'),
    path('library/user/<int:user_id>/', views.user_books, name='user_books'),
    path('library/user/add/', views.add_user, name='add_user'),
    path('library/book/<int:book_id>/', views.book, name='book'),
    path('library/book/add/', views.add_book, name='add_book'),
    path('library/book/<int:book_id>/change/', views.change_book, name='change_book'),
    path('library/book/<int:book_id>/delete/', views.delete_book, name='delete_book'),
    path('api/v1/library/user/add/', views.user_create_view.as_view(), name='api_user_add'),
    path('api/v1/library/user/<int:pk>/', views.user_detail_view.as_view(), name='api_user_detail'),
    path('api/v1/library/user/<int:pk>/edit', views.user_edit_view.as_view(), name='api_user_edit'),
    path('api/v1/library/user/<int:pk>/delete', views.user_delete_view.as_view(), name='api_user_delete'),
    path('api/v1/library/user/all/', views.user_list_view.as_view(), name='api_user_list'),
    path('api/v1/library/book/add/', views.book_create_view.as_view(), name='api_book_add'),
    path('api/v1/library/book/<int:pk>/', views.book_detail_view.as_view(), name='api_book_detail'),
    path('api/v1/library/book/<int:pk>/edit', views.book_create_view.as_view(), name='api_book_edit'),
    path('api/v1/library/book/<int:pk>/delete', views.book_delete_view.as_view(), name='api_book_delete'),
    path('api/v1/library/book/all/', views.book_list_view.as_view(), name='api_book_list'),
]
