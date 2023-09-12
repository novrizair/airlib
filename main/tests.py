from django.test import TestCase, Client

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertNotEqual(response.status_code, 404) # 404 = not found, kalo 200 = ok (ada)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

# COLLABORATOR: SABRINA ATHA SHANIA
# REFERENSI: https://www.geeksforgeeks.org/python-unittest-assertnotequal-function/
#            https://www.semrush.com/blog/what-does-error-404-not-found-mean/