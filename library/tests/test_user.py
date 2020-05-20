from rest_framework.test import APIRequestFactory, APITestCase, force_authenticate
from rest_framework.reverse import reverse
from ..models import User
from .. import views


class Helper(APITestCase):
    def get_helper(self, force, code, kwargs=False, user=User):
        if kwargs == False:
            request = self.factory.get(self.url)
        else:
            request = self.factory.get(self.url, uid=user.id)
        if force == True:
            force_authenticate(request, user=user)
        # print(request.build_absolute_uri())
        if kwargs == False:
            response = self.view(request)
        else:
            response = self.view(request, uid=user.id)
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


class TestLibraryUserList(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('library:api_user_list')
        self.view = views.UserListView.as_view()
        self.user = User.objects.create(username='John')

    def test_GetUserList(self):
        Helper.get_helper(self, force=True, code=200)


class TestLibraryUserAdd(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('library:api_user_add')
        self.view = views.UserCreateView.as_view()
        self.user = User.objects.create(username='John')

    def test_get_add_user(self):
        Helper.get_helper(self, force=True, code=405)

    def test_add_user(self):
        Helper.post_helper(self, data={"username": "TestUser"}, force=True, code=201)

    def test_add_empty_user(self):
        Helper.post_helper(self, data={"username": ""}, force=True, code=400)

    def test_unauthorized_add_user(self):
        Helper.post_helper(self, data={"username": "TestUser"}, force=False, code=401)

    def test_forbidden_add_user(self):
        Helper.post_helper(self, data={"username": "TestUser"}, force=True, code=403, user=self.user)


class TestLibraryUserDetail(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='John')
        self.superuser = User.objects.create_superuser(username="Admin")
        self.factory = APIRequestFactory()
        self.view = views.UserDetailView.as_view()
        self.url = reverse('library:api_user_detail', kwargs={'uid': self.user.id})

    def test_user_detail(self):
        Helper.get_helper(self, force=True, code=200, kwargs=True, user=self.superuser)

    def test_unauthorised_user_detail(self):
        Helper.get_helper(self, force=False, code=401, kwargs=True, user=self.user)

    def test_forbidden_user_detail(self):
        Helper.get_helper(self, force=True, code=403, kwargs=True, user=self.user)


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
        response = self.view(request, uid=self.user.id)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))


class TestLibraryUserDelete(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username='Admin')
        user = User.objects.create(username="John")
        user.save()
        self.factory = APIRequestFactory()
        self.view = views.UserDeleteView.as_view()
        self.url = reverse('library:api_user_delete', kwargs={'uid': user.id})

    def test_user_delete(self):
        request = self.factory.post(self.url, uid=self.user.id)
        force_authenticate(request, user=self.user, token=self.user)
        response = self.view(request, uid=self.user.id)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))
