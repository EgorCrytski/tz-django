from rest_framework.test import APIRequestFactory, APITestCase, force_authenticate
from rest_framework.reverse import reverse
from .models import User, Book
from . import views
import datetime


class TestLibraryUserList(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('library:api_user_list')
        self.view = views.UserListView.as_view()

    def test_GetUserList(self):
        user = User
        request = self.factory.get(self.url)
        force_authenticate(request, user=user, token=user.auth_token)
        response = self.view(request)
        print('\n' + request.build_absolute_uri())
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))


class TestLibraryUserAdd(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('library:api_user_add')
        self.view = views.UserCreateView.as_view()
        self.user = User.objects.create(username='admin')

    def test_get_add_user(self):
        user = User
        request = self.factory.get(self.url)
        force_authenticate(request, user=user, token=user.auth_token)
        response = self.view(request)
        print('\n' + request.build_absolute_uri())
        self.assertEqual(response.status_code, 405,
                         'Expected Response Code 405, received {0} instead.'
                         .format(response.status_code))

    def test_add_user(self):
        user = User
        request = self.factory.post(self.url, {"username": "TestUser"}, format='json')
        force_authenticate(request, user=user, token=user.auth_token)
        response = self.view(request)
        print('\n' + request.build_absolute_uri())
        self.assertEqual(response.status_code, 201,
                         'Expected Response Code 201, received {0} instead.'
                         .format(response.status_code))

    def test_add_empty_user(self):
        user = User
        request = self.factory.post(self.url, {"username": ""}, format='json')
        force_authenticate(request, user=user, token=user.auth_token)
        response = self.view(request)
        print('\n' + request.build_absolute_uri())
        self.assertEqual(response.status_code, 400,
                         'Expected Response Code 400, received {0} instead.'
                         .format(response.status_code))

    def test_unauthorized_add_user(self):
        user = User
        request = self.factory.post(self.url, {"username": "TestUser"}, format='json')
        # force_authenticate(request, user=user, token=user.auth_token)
        response = self.view(request)
        print('\n' + request.build_absolute_uri())
        self.assertEqual(response.status_code, 401,
                         'Expected Response Code 401, received {0} instead.'
                         .format(response.status_code))

    def test_forbidden_add_user(self):

        request = self.factory.post(self.url, {"username": "TestUser"}, format='json')
        force_authenticate(request, user=self.user, token=self.user)
        response = self.view(request)
        print('\n' + request.build_absolute_uri())
        self.assertEqual(response.status_code, 403,
                         'Expected Response Code 403, received {0} instead.'
                         .format(response.status_code))


class TestLibraryUserDetail(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='John')
        self.factory = APIRequestFactory()
        self.view = views.UserDetailView.as_view()

    def test_user_detail(self):
        user = User
        self.url = reverse('library:api_user_detail', kwargs={'uid': self.user.id})
        request = self.factory.get(self.url, uid=self.user.id)
        force_authenticate(request, user=user, token=user.auth_token)
        print('\n' + request.build_absolute_uri())
        response = self.view(request, uid=self.user.id)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))

    def test_unauthorised_user_detail(self):

        self.url = reverse('library:api_user_detail', kwargs={'uid': self.user.id})
        request = self.factory.get(self.url, uid=self.user.id)
        #force_authenticate(request, user=user, token=self.user.auth_token)
        print('\n' + request.build_absolute_uri())
        response = self.view(request, uid=self.user.id)
        self.assertEqual(response.status_code, 401,
                         'Expected Response Code 401, received {0} instead.'
                         .format(response.status_code))

    def test_forbidden_user_detail(self):
        user = User
        self.url = reverse('library:api_user_detail', kwargs={'uid': self.user.id})
        request = self.factory.get(self.url, uid=self.user.id)
        force_authenticate(request, user=self.user, token=self.user)
        print('\n' + request.build_absolute_uri())
        response = self.view(request, uid=self.user.id)
        self.assertEqual(response.status_code, 403,
                         'Expected Response Code 403, received {0} instead.'
                         .format(response.status_code))


class TestLibraryUserEdit(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='John')
        self.factory = APIRequestFactory()
        self.view = views.UserEditView.as_view()

    def test_user_edit(self):
        user = User
        self.url = reverse('library:api_user_edit', kwargs={'uid': self.user.id})
        request = self.factory.put(self.url, data={"username": "Mark"}, uid=self.user.id)
        force_authenticate(request, user=user, token=user)
        print('\n' + request.build_absolute_uri())
        response = self.view(request, uid=self.user.id)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))


class TestLibraryUserDelete(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='John')
        self.factory = APIRequestFactory()
        self.view = views.UserDeleteView.as_view()

    def test_user_delete(self):
        user = User
        self.url = reverse('library:api_user_delete', kwargs={'uid': self.user.id})
        request = self.factory.post(self.url, uid=user.id)
        force_authenticate(request, user=user, token=user)
        print('\n' + request.build_absolute_uri())
        response = self.view(request, uid=self.user.id)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))


class TestLibraryBookList(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('library:api_book_list')
        self.view = views.BookListView.as_view()

    def test_get_book_list(self):
        user = User
        request = self.factory.get(self.url)
        force_authenticate(request, user=user, token=user.auth_token)
        response = self.view(request)
        print('\n' + request.build_absolute_uri())
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))


class TestLibraryBookAdd(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='John')
        self.factory = APIRequestFactory()
        self.url = reverse('library:api_book_add', )
        self.view = views.BookCreateView.as_view()

    def test_get_add_book(self):
        user = User
        request = self.factory.get(self.url)
        force_authenticate(request, user=user, token=user)
        response = self.view(request)
        print('\n' + request.build_absolute_uri())
        self.assertEqual(response.status_code, 405,
                         'Expected Response Code 405, received {0} instead.'
                         .format(response.status_code))

    def test_add_book(self):
        user = User
        request = self.factory.post(self.url, {"book_name": "test book",
                                               "book_author": "test author",
                                               "book_year": datetime.datetime.now(),
                                               "user": self.user.id}, format='json')
        force_authenticate(request, user=user, token=user)
        response = self.view(request)
        print('\n' + request.build_absolute_uri())
        self.assertEqual(response.status_code, 201,
                         'Expected Response Code 201, received {0} instead.'
                         .format(response.status_code))

    def test_add_empty_book(self):
        user = User
        request = self.factory.post(self.url, {"book_name": "",
                                               "book_author": "test author",
                                               "book_year": datetime.datetime.now(),
                                               "user": self.user.id}, format='json')
        force_authenticate(request, user=user, token=user)
        response = self.view(request)
        print('\n' + request.build_absolute_uri())
        self.assertEqual(response.status_code, 400,
                         'Expected Response Code 400, received {0} instead.'
                         .format(response.status_code))


class TestLibraryBookDetail(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='John')
        self.book = Book.objects.create(book_name="Book",
                                        book_author="Author",
                                        book_year=datetime.datetime.now(),
                                        user=self.user)
        self.factory = APIRequestFactory()
        self.view = views.BookDetailView.as_view()

    def test_book_detail(self):
        user = User
        self.url = reverse('library:api_book_detail', kwargs={'uid': self.user.id, 'bid': 1})
        request = self.factory.get(self.url, uid=self.user.id, bid=1)
        force_authenticate(request, user=user, token=user)
        print('\n' + request.build_absolute_uri())
        response = self.view(request, uid=self.user.id, bid=1)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))


class TestLibraryBookEdit(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='John')
        self.book = Book.objects.create(book_name="Book",
                                        book_author="Author",
                                        book_year=datetime.datetime.now(),
                                        user=self.user)
        self.factory = APIRequestFactory()
        self.view = views.BookEditView.as_view()

    def test_book_edit(self):
        user = User
        self.url = reverse('library:api_book_edit', kwargs={'uid': self.user.id, 'bid': 1})
        request = self.factory.put(self.url, data={"book_name": "book1",
                                                   "book_author": "author1",
                                                   "book_year": "1212-12-21T00:00:00Z", }
                                   , bid=1, uid=self.user.id)
        print('\n' + request.build_absolute_uri())
        force_authenticate(request, user=user, token=user)
        response = self.view(request, bid=1, uid=self.user.id)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))


class TestLibraryBookDelete(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='John')
        self.book = Book.objects.create(book_name="Book",
                                        book_author="Author",
                                        book_year=datetime.datetime.now(),
                                        user=self.user)
        self.factory = APIRequestFactory()
        self.view = views.BookDeleteView.as_view()

    def test_book_delete(self):
        user = User
        self.url = reverse('library:api_book_delete', kwargs={'uid': self.user.id, 'bid': 1})
        request = self.factory.post(self.url, uid=self.user.id, bid=1)
        force_authenticate(request, user=user, token=user)
        print('\n' + request.build_absolute_uri())
        response = self.view(request, uid=self.user.id, bid=1)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))
