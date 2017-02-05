"""
Test the index view is being accessed properly.
"""


from django.test import TestCase, Client
from django.urls import reverse

class TestIndexView(TestCase):
    client = None

    def setUp(self):
        self.client = Client()

    def test_view_init(self):
        """Test the view can be accessed from the url."""
        res = self.client.get("")
        self.assertEquals(res.status_code, 302)
        redirect = res._headers['location'][1]
        self.assertTrue('app' in redirect)

        res = self.client.get(redirect)
        self.assertEqual(res.status_code, 200)
        
