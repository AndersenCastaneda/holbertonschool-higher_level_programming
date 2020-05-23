#!/usr/bin/python3
"""Unittest for max_integer([..]) Module
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """TestSuite for max_integer function"""

    def test_none(self):
        """Test empty list. Return None"""
        self.assertIsNone(max_integer([]), True)
        self.assertEqual(max_integer([]), None)

    def test_positive_num(self):
        """Test positive value. Return True"""
        self.assertTrue(max_integer([98]))

    def test_empty(self):
        """Test 0 value. Return 0 (False)"""
        self.assertFalse(max_integer([]))
        self.assertFalse(max_integer([0]))

    def test_large_list(self):
        """Test list of integers. Return max value"""
        self.assertEqual(max_integer([-3, -12, -98, -46, -128, -716, -1, -6, -32.3]), -1)
        self.assertEqual(max_integer([-3, -12, -98, -46, -128, -716, -1, -6, 32.3]), 32.3)

    def test_string(self):
        """Test string values. Return max value in ascii"""
        self.assertEqual(max_integer(["Hello", "World"]), "World")
        self.assertEqual(max_integer(["A", "B"]), "B")

    def test_combined_types(self):
        """Test whit different types. Return TypeError"""
        self.assertRaises(TypeError, max_integer, ["A", 2])
        self.assertRaises(TypeError, max_integer, [4, "A", "B"])

    def test_no_list(self):
        """Test whit no lost type. Return TypeError"""
        self.assertRaises(TypeError, max_integer, 98)
