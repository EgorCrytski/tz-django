from django import test


class URLTests(test.TestCase):
    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 404)

    def test_user_books(self):
        response = self.client.get('/user/1/')
        # self.assertEqual(response.status_code, 404)

    def test_user_add(self):
        response = self.client.post('/user/add/', {'username': 'john'})
        # self.assertEqual(response.status_code, 201)
