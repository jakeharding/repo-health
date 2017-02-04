"""
Test the index view is being accessed properly.
"""


from django.test import TestCase, Client

class TestIndexView(TestCase):
    client = None

    def setUp(self):
        self.client = Client()

    def test_view_init(self):
        """Test the view can be accessed from the url.'''
        res = self.client.get("")
        self.assertEquals(res.status_code, 200)
        #Python 3 changed the way strings and bytes work. The `b` here converts the string to bytes.
        self.assertTrue(b"Hello World" in res.content)
        
