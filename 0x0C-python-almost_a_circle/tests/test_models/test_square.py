#!/usr/bin/python3
"""Test Square Module

    imports:
        unittest
        pep8
        models.square
"""

import unittest
import pep8
from models.square import Square


class TestSquare(unittest.TestCase):
    """TestBase class to test class Base"""

    def test_pep8_Base(self):
        """Test base.py pep8 style"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0)

    def test_pep8_TestBase(self):
        """Test test_base.py pep8 style"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_rectangle.py'])
        self.assertEqual(result.total_errors, 0)

    def test_rectangle_instantation(self):
        pass

    def test_str(self):
        pass

    def test_size(self):
        pass

    def test_x(self):
        pass

    def test_y(self):
        pass

    def test_update(self):
        pass

    def test_to_dictionary(self):
        pass
