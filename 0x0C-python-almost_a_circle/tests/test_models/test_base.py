#!usr/bin/python3
"""Test Base Module

    imports:
        unit test
        pep8
        models.base
        models.rectangle
        models.square
"""

import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """TestBase class to test class Base"""

    def test_pep8_Base(self):
        """Test base.py pep8 style"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/base.py'])
        self.assertEqual(result.total_errors, 0)

    def test_pep8_TestBase(self):
        """Test test_base.py pep8 style"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_base.py'])
        self.assertEqual(result.total_errors, 0)

    def test_base_no_id(self):
        """Test instance creation whitout set id"""
        obj = Base()
        self.assertIsInstance(obj, Base)
        self.assertEqual(obj.id, 1)
        obj = Base()
        self.assertIsInstance(obj, Base)
        self.assertEqual(obj.id, 2)

    def test_base_set_id(self):
        """Test instance creation setting id to int"""
        obj = Base(12)
        self.assertIsInstance(obj, Base)
        self.assertEqual(obj.id, 12)
        obj = Base(17)
        self.assertIsInstance(obj, Base)
        self.assertEqual(obj.id, 17)

    def test_base_set_id_none(self):
        """Test instance creation setting id to None"""
        with self.assertRaises(TypeError) as e:
            obj = Base("12")
            self.assertTrue("id must be an integer" in str(e.exception))
            obj = Base(12.1)
            self.assertTrue("id must be an integer" in str(e.exception))

    def test_base_to_json_string(self):
        """Test to_json_string()"""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertIsInstance(json_dictionary, str)

        json_dictionary = Base.to_json_string([])
        self.assertEqual(json_dictionary, '[]')

        with self.assertRaises(TypeError) as e:
            json_dictionary = Base.to_json_string("12")
            self.assertTrue("list_dictionaries must be a list of dictionaries"
                            in str(e.exception))
