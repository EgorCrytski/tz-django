from rest_framework.test import APIRequestFactory, APITestCase
from rest_framework.reverse import reverse
from .models import User, Book
from . import apiviews
import datetime


class TestLibraryUserList(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('api:user_list')
        self.view = apiviews.UserListView.as_view()

    def test_GetUserList(self):
        request = self.factory.get(self.url)
        response = self.view(request)
        print('\n' + request.build_absolute_uri())
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))


class TestLibraryUserAdd(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('api:user_add')
        self.view = apiviews.UserCreateView.as_view()

    def test_GetAddUser(self):
        request = self.factory.get(self.url)
        response = self.view(request)
        print('\n' + request.build_absolute_uri())
        self.assertEqual(response.status_code, 405,
                         'Expected Response Code 405, received {0} instead.'
                         .format(response.status_code))

    def test_AddUser(self):
        request = self.factory.post(self.url, {"user_name": "TestUser"}, format='json')
        response = self.view(request)
        print('\n' + request.build_absolute_uri())
        self.assertEqual(response.status_code, 201,
                         'Expected Response Code 201, received {0} instead.'
                         .format(response.status_code))

    def test_AddEmptyUser(self):
        request = self.factory.post(self.url, {"user_name": ""}, format='json')
        response = self.view(request)
        print('\n' + request.build_absolute_uri())
        self.assertEqual(response.status_code, 400,
                         'Expected Response Code 400, received {0} instead.'
                         .format(response.status_code))


class TestLibraryUserDetail(APITestCase):
    def setUp(self):
        self.user = User.objects.create(user_name='John')
        self.factory = APIRequestFactory()
        self.view = apiviews.UserDetailView.as_view()

    def test_UserDetail(self):
        self.url = reverse('api:user_detail', kwargs={'pk': self.user.id})
        request = self.factory.get(self.url, pk=self.user.id)
        print('\n' + request.build_absolute_uri())
        response = self.view(request, pk=self.user.id)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))


class TestLibraryUserEdit(APITestCase):
    def setUp(self):
        self.user = User.objects.create(user_name='John')
        self.factory = APIRequestFactory()
        self.view = apiviews.UserEditView.as_view()

    def test_UserEdit(self):
        self.url = reverse('api:user_edit', kwargs={'pk': self.user.id})
        request = self.factory.put(self.url, data={"user_name": "Mark"}, pk=self.user.id)
        print('\n' + request.build_absolute_uri())
        response = self.view(request, pk=self.user.id)
        self.assertEqual(response.status_code, 202,
                         'Expected Response Code 202, received {0} instead.'
                         .format(response.status_code))


class TestLibraryUserDelete(APITestCase):
    def setUp(self):
        self.user = User.objects.create(user_name='John')
        self.factory = APIRequestFactory()
        self.view = apiviews.UserDeleteView.as_view()

    def test_UserDelete(self):
        self.url = reverse('api:user_delete', kwargs={'pk': self.user.id})
        request = self.factory.post(self.url, pk=self.user.id)
        print('\n' + request.build_absolute_uri())
        response = self.view(request, pk=self.user.id)
        self.assertEqual(response.status_code, 202,
                         'Expected Response Code 202, received {0} instead.'
                         .format(response.status_code))


class TestLibraryBookList(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('api:book_list')
        self.view = apiviews.BookListView.as_view()

    def test_GetBookList(self):
        request = self.factory.get(self.url)
        response = self.view(request)
        print('\n' + request.build_absolute_uri())
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))


class TestLibraryBookAdd(APITestCase):
    def setUp(self):
        self.user = User.objects.create(user_name='John')
        self.factory = APIRequestFactory()
        self.url = reverse('api:book_add')
        self.view = apiviews.BookCreateView.as_view()

    def test_GetAddBook(self):
        request = self.factory.get(self.url)
        response = self.view(request)
        print('\n' + request.build_absolute_uri())
        self.assertEqual(response.status_code, 405,
                         'Expected Response Code 405, received {0} instead.'
                         .format(response.status_code))

    def test_AddBook(self):
        request = self.factory.post(self.url, {"book_name": "test book",
                                               "book_author": "test author",
                                               "book_year": datetime.datetime.now(),
                                               "user": self.user.id}, format='json')
        response = self.view(request)
        print('\n' + request.build_absolute_uri())
        self.assertEqual(response.status_code, 201,
                         'Expected Response Code 201, received {0} instead.'
                         .format(response.status_code))

    def test_AddEmptyBook(self):
        request = self.factory.post(self.url, {"book_name": "",
                                               "book_author": "test author",
                                               "book_year": datetime.datetime.now(),
                                               "user": self.user.id}, format='json')
        response = self.view(request)
        print('\n' + request.build_absolute_uri())
        self.assertEqual(response.status_code, 400,
                         'Expected Response Code 400, received {0} instead.'
                         .format(response.status_code))


class TestLibraryBookDetail(APITestCase):
    def setUp(self):
        self.user = User.objects.create(user_name='John')
        self.book = Book.objects.create(book_name="Book",
                                        book_author="Author",
                                        book_year=datetime.datetime.now(),
                                        user=self.user)
        self.factory = APIRequestFactory()
        self.view = apiviews.BookDetailView.as_view()

    def test_BookDetail(self):
        self.url = reverse('api:book_detail', kwargs={'pk': self.book.id})
        request = self.factory.get(self.url, pk=self.book.id)
        print('\n' + request.build_absolute_uri())
        response = self.view(request, pk=self.book.id)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))

class TestLibraryBookEdit(APITestCase):
    def setUp(self):
        self.user = User.objects.create(user_name='John')
        self.book = Book.objects.create(book_name="Book",
                                        book_author="Author",
                                        book_year=datetime.datetime.now(),
                                        user=self.user)
        self.factory = APIRequestFactory()
        self.view = apiviews.BookEditView.as_view()

    def test_BookEdit(self):
        self.url = reverse('api:book_edit', kwargs={'pk': self.book.id})
        request = self.factory.put(self.url, data = {"book_name": "book1",
                                                     "book_author": "author1",
                                                     "book_year": "1212-12-21T00:00:00Z",}
                                   , pk=self.book.id)
        print('\n' + request.build_absolute_uri())
        response = self.view(request, pk=self.book.id)
        self.assertEqual(response.status_code, 202,
                         'Expected Response Code 202, received {0} instead.'
                         .format(response.status_code))


class TestLibraryBookDelete(APITestCase):
    def setUp(self):
        self.user = User.objects.create(user_name='John')
        self.book = Book.objects.create(book_name="Book",
                                        book_author="Author",
                                        book_year=datetime.datetime.now(),
                                        user=self.user)
        self.factory = APIRequestFactory()
        self.view = apiviews.BookDeleteView.as_view()

    def test_BookDelete(self):
        self.url = reverse('api:book_delete', kwargs={'pk': self.book.id})
        request = self.factory.post(self.url, pk=self.book.id)
        print('\n' + request.build_absolute_uri())
        response = self.view(request, pk=self.book.id)
        self.assertEqual(response.status_code, 202,
                         'Expected Response Code 202, received {0} instead.'
                         .format(response.status_code))