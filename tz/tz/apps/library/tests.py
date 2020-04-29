from rest_framework.test import APIRequestFactory, APITestCase
from rest_framework.reverse import reverse
from .models import User, Book
from . import apiviews
import datetime


class TestLibrary(APITestCase):
    def setUp(self):
        user1 = User(user_name='John') #1
        user2 = User(user_name='Mark') #2
        user3 = User(user_name='Peter') #3
        user1.save()
        user2.save()
        user3.save()
        self.factory = APIRequestFactory()
        #self.url = list_url

        book1 = Book(book_name='book 1', book_author='author 1',
             book_year=datetime.datetime.now(), user_id=user1)
        book2 = Book(book_name='book 2', book_author='author 2',
             book_year=datetime.datetime.now(), user_id=user1)
        book3 = Book(book_name='book 3', book_author='author 3',
             book_year=datetime.datetime.now(), user_id=user2)
        book1.save()
        book2.save()
        book3.save()

    def test_UserAll(self):
        self.url = reverse('api:user_list')
        self.view = apiviews.UserListView.as_view()
        request = self.factory.get(self.url)
        print('\ntest\n')
        response = self.view(request)
        print(request.build_absolute_uri())
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))
