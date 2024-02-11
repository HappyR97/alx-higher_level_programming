#!/usr/bin/python3

"""

Unittests for max_integer

"""

import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """ Defines unit tests for max_integer """

    def test_list(self):
        """ Test a normal list """
        list = [1, 2, 3, 4]
        self.assertEqual(max_integer(list), 4)

    def test_list_unordered(self):
        """ Tests an unordered list """
        list_unordered = [4, 0, 6, 1]
        self.assertEqual(max_integer(list_unordered), 6)

    def test_max_first(self):
        """ Test a list with max value at first index """
        max_first = [100, 20, 33, 70]
        self.assertEqual(max_integer(max_first), 100)

    def text_max_last(self):
        """ Test a list with max value at last index """
        max_last = [2, 0, 7, 10]
        self.assertEqual(max_integer(max_last), 10)

    def test_emplty(self):
        """ Tests an empty list """
        list_empty = []
        self.assertEqual(max_integer(list_empty), None)

    def test_one_element(self):
        """ Tests a list with one element """
        one_element = [10]
        self.assertEqual(max_integer(one_element), 10)

    def test_floats(self):
        """ Tests a list with floats only """
        list_floats = [1.6, 2.9, 4.5, 9.1]
        self.assertEqual(max_integer(list_floats), 9.1)

    def test_mixed(self):
        """ Tests a list with mixed ints and floats """
        list_mixed = [1, 10, 2.6, 7.1]
        self.assertEqual(max_integer(list_mixed), 10)

    def test_string(self):
        """ Tests a string """
        string = "abcdef"
        self.assertEqual(max_integer(string), 'f')

    def test_strings(self):
        """ Tests a list of strings """
        strings = ["Hakuna", "Matata"]
        self.assertEqual(max_integer(strings), "Matata")

    def test_empty_string(self):
        """ Tests an empty string """
        empty_string = ""
        self.assertEqual(max_integer(empty_string), None)


if __name__ == '__main__':
    unittest.main()
