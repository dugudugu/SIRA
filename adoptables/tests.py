from django.test import TestCase
from .models import Adoptable

# Create your tests here.
class AdoptableTests(TestCase):

# Test to return a adoptable dog name
    def test_str(self):
        test_name = Adoptable(name='A dog name')
        self.assertEqual(str(test_name), 'A dog name')