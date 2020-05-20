from datetime import datetime
from rest_framework.test import APIRequestFactory, APITestCase, force_authenticate
from rest_framework.reverse import reverse
from ..models import User, Book
from .. import views


class Helper(APITestCase):
    def get_helper(self, force, code, kwargs=False, user=User):
        if kwargs == False:
            request = self.factory.get(self.url)
        else:
            request = self.factory.get(self.url, uid=self.user.id, bid=1)
        if force == True:
            force_authenticate(request, user=user)
        if kwargs == False:
            response = self.view(request)
        else:
            response = self.view(request, uid=self.user.id, bid=1)
        self.assertEqual(response.status_code, code,
                         'Expected Response Code {0}, received {1} instead.'
                         .format(code, response.status_code))

    def post_helper(self, data, force, code, user=User):
        request = self.factory.post(self.url, data, format='json')
        if force == True:
            force_authenticate(request, user=user)
        response = self.view(request)
        self.assertEqual(response.status_code, code,
                         'Expected Response Code {0}, received {1} instead.'
                         .format(code, response.status_code))


class TestLibraryBookList(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('library:api_book_list')
        self.view = views.BookListView.as_view()
        self.user = User.objects.create_superuser(username='Admin')

    def test_get_book_list(self):
        Helper.get_helper(self, force=True, code=200, user=self.user)


class TestLibraryBookAdd(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username='Admin')
        self.factory = APIRequestFactory()
        self.url = reverse('library:api_book_add', )
        self.view = views.BookCreateView.as_view()

    def test_get_add_book(self):
        Helper.get_helper(self, force=True, code=405, user=self.user)

    def test_add_book(self):
        Helper.post_helper(self, {"book_name": "test book",
                                  "book_author": "test author",
                                  "book_year": datetime.now(),
                                  "user": self.user.id}, force=True, code=201, user=self.user)

    def test_add_empty_book(self):
        Helper.post_helper(self, {"book_name": "",
                                  "book_author": "test author",
                                  "book_year": datetime.now(),
                                  "user": self.user.id}, force=True, code=400, user=self.user)


class TestLibraryBookDetail(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username='Admin')
        self.book = Book.objects.create(book_name="Book",
                                        book_author="Author",
                                        book_year=datetime.now(),
                                        user=self.user)
        self.factory = APIRequestFactory()
        self.view = views.BookDetailView.as_view()
        self.url = reverse('library:api_book_detail', kwargs={'uid': self.user.id, 'bid': 1})

    def test_book_detail(self):
        Helper.get_helper(self, force=True, code=200, kwargs=True, user=self.user)


class TestLibraryBookEdit(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='John')
        self.book = Book.objects.create(book_name="Book",
                                        book_author="Author",
                                        book_year=datetime.now(),
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
                                        book_year=datetime.now(),
                                        user=self.user)
        self.factory = APIRequestFactory()
        self.view = views.BookDeleteView.as_view()

    def test_book_delete(self):
        user = User
        self.url = reverse('library:api_book_delete', kwargs={'uid': self.user.id, 'bid': 1})
        request = self.factory.post(self.url, uid=self.user.id, bid=1)
        force_authenticate(request, user=user, token=user)
        response = self.view(request, uid=self.user.id, bid=1)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))
