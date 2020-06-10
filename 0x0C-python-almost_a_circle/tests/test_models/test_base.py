#!/usr/bin/python3
"""Test Base Module

    imports:
        unittest
        pep8
        os.path
        models.base
        models.rectangle
        models.square
"""

import unittest
import pep8
import os.path as path
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """TestBase class to test class Base"""

    def test_base_pep8(self):
        """Test base.py pep8 style"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/base.py'])
        self.assertEqual(result.total_errors, 0)

    def test_pep8_self(self):
        """Test test_base.py pep8 style"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_base.py'])
        self.assertEqual(result.total_errors, 0)

    def test_base_1_no_id(self):
        """Test instance creation whitout set id"""
        obj = Base()
        self.assertIsInstance(obj, Base)
        self.assertEqual(obj.id, 1)
        obj = Base()
        self.assertIsInstance(obj, Base)
        self.assertEqual(obj.id, 2)

    def test_base_2_set_id(self):
        """Test instance creation setting id to int"""
        obj = Base(12)
        self.assertIsInstance(obj, Base)
        self.assertEqual(obj.id, 12)
        obj = Base(17)
        self.assertIsInstance(obj, Base)
        self.assertEqual(obj.id, 17)

    def test_base_3_set_id_to_exception(self):
        """Test instance creation setting id to None"""
        with self.assertRaises(TypeError) as e:
            obj = Base("12")
            self.assertTrue("id must be an integer" in str(e.exception))
            obj = Base(12.1)
            self.assertTrue("id must be an integer" in str(e.exception))

    def test_base_4_to_json_string(self):
        """Test to_json_string()"""
        r1 = Rectangle(10, 7, 2, 8, 20)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertIsInstance(json_dictionary, str)

        empty_dictionary = Base.to_json_string([])
        self.assertEqual(empty_dictionary, '[]')

        with self.assertRaises(TypeError) as e:
            error_dictionary = Base.to_json_string("12")
            self.assertTrue("list_dictionaries must be a list of dictionaries"
                            in str(e.exception))

    def test_base_5_from_json_string(self):
        """Test from_json_string()"""
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_base_6_create(self):
        """Test create()"""
        r1 = Rectangle(3, 5, 1, 4, 16)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsInstance(r1, Rectangle)
        self.assertIsInstance(r2, Rectangle)
        self.assertEqual(r1.id, r2.id)

        s1 = Square(12, 3, 4, 98)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertIsInstance(s1, Square)
        self.assertIsInstance(s2, Square)
        self.assertEqual(s1.id, s2.id)

    def test_base_7_save_to_file(self):
        """Test save_to_file()"""
        Rectangle.save_to_file([])
        self.assertTrue(path.exists("Rectangle.json"))

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(4, 6, 3)
        Rectangle.save_to_file([r1, r2])
        self.assertTrue(path.exists("Rectangle.json"))

    def test_base_8_load_from_file(self):
        """Test load_from_file()"""
        Rectangle.save_to_file([])
        lobj = Rectangle.load_from_file()
        self.assertEqual(lobj, [])

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertTrue(
            all(type(elem) == Rectangle for elem in list_rectangles_output))
