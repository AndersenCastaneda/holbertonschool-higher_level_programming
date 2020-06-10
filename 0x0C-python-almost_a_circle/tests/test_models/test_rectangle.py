#!/usr/bin/python3
"""Test Rectangle Module

    imports:
        unittest
        pep8
        models.rectangle
"""

import unittest
import pep8
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
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

    def test_width(self):
        pass

    def test_height(self):
        pass

    def test_x(self):
        pass

    def test_y(self):
        pass

    def test_area(self):
        pass

    def test_display(self):
        pass

    def test_update(self):
        pass

    def test_to_dictionary(self):
        pass
