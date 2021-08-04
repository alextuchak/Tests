import unittest
from Functions import shelf, add, delete


class functions_unittest(unittest.TestCase):

    def setUp(self):
        print('method setUp')

    def tearDown(self):
        print('method tearDown')

    def test_shelf_true(self):
        self.assertEqual('2', shelf('10006'))

    def test_shelf_false(self):
        self.assertEqual(None, shelf('11111'))

    def test_add(self):
        self.assertEqual('3', add('SSN', '1234', 'Alex', '3'))

    def test_delete(self):
        self.assertEqual(True, delete('11-2'))
