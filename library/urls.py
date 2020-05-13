from django.urls import path

from . import views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, TokenVerifyView)


app_name = 'library'

urlpatterns = [
    path('', views.index, name='index'),
    path('library/user/<int:user_id>/', views.user_books, name='user_books'),
    path('library/user/add/', views.add_user, name='add_user'),

    path('library/book/<int:book_id>/', views.book, name='book'),
    path('library/book/add/', views.add_book, name='add_book'),
    path('library/book/<int:book_id>/change/', views.change_book, name='change_book'),
    path('library/book/<int:book_id>/delete/', views.delete_book, name='delete_book'),

    path('api/v1/library/user/add/', views.UserCreateView.as_view(), name='api_user_add'),
    path('api/v1/library/user/<int:uid>/', views.UserDetailView.as_view(), name='api_user_detail'),
    path('api/v1/library/user/me/', views.SelfUserDetailView().as_view(), name='api_self_user_detail'),
    path('api/v1/library/user/<int:uid>/edit/', views.UserEditView.as_view(), name='api_user_edit'),
    path('api/v1/library/user/<int:uid>/delete/', views.UserDeleteView.as_view(), name='api_user_delete'),
    path('api/v1/library/user/all/', views.UserListView.as_view(), name='api_user_list'),

    path('api/v1/library/book/add/', views.BookCreateView.as_view(), name='api_book_add'),
    path('api/v1/library/book/add/myself/', views.SelfBookCreateView.as_view(), name='api_self_book_add'),
    path('api/v1/library/user/<int:uid>/book/<int:bid>/', views.BookDetailView.as_view(), name='api_book_detail'),
    path('api/v1/library/user/<int:uid>/book/<int:bid>/edit/', views.BookEditView.as_view(), name='api_book_edit'),
    path('api/v1/library/user/<int:uid>/book/<int:bid>/delete/', views.BookDeleteView.as_view(), name='api_book_delete'),
    path('api/v1/library/book/all/', views.BookListView.as_view(), name='api_book_list'),
    path('api/v1/token/', TokenObtainPairView.as_view(), name = 'token'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view()),
    path('api/v1/token/verify/', TokenVerifyView.as_view()),
]
