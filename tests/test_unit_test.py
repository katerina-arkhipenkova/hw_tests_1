import unittest
from parameterized import parameterized
from unittest.mock import patch
from main import get_doc_owner_name, get_all_doc_owners_names, add_new_shelf, delete_doc, get_doc_shelf, add_new_doc


class TestFunctions(unittest.TestCase):
    def setUp(self) -> None:
        ...

    def tearDown(self) -> None:
        ...

    @classmethod
    def setUpClass(cls) -> None:
        ...

    @classmethod
    def tearDownClass(cls) -> None:
        ...

    def test_get_all_doc_owners_names(self):
        result = {'Аристарх Павлов', 'Геннадий Покемонов', 'Василий Гупкин'}
        self.assertEqual(get_all_doc_owners_names(), result)

    @patch('builtins.input', return_value='2207 876234')
    def test_get_doc_owner_name(self, *args, **kwargs):
        result = 'Василий Гупкин'
        self.assertEqual(get_doc_owner_name(), result)

    @patch('builtins.input', return_value='2207 876234')
    def test_get_doc_shelf(self, *args, **kwargs):
        result = '1'
        self.assertEqual(get_doc_shelf(), result)

    @patch('builtins.input', return_value='5')
    def test_add_new_shelf(self, *args, **kwargs):
        result = '5', True
        self.assertEqual(add_new_shelf(), result)

    @patch('builtins.input', return_value='10006')
    def test_delete_doc(self, *args, **kwargs):
        result = '10006', True
        self.assertEqual(delete_doc(), result)

    @patch('builtins.input', return_value='2')
    @patch('builtins.input', return_value='Иван Иванов')
    @patch('builtins.input', return_value='passport')
    @patch('builtins.input', return_value='1234 567890')
    def test_add_new_doc(self, *args, **kwargs):
        result = '2'
        self.assertEqual(add_new_doc(), result)
