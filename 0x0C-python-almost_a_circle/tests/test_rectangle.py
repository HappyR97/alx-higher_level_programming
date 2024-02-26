#!/usr/bin/python3
"""

This is a unitest for Rectangle class

"""
from models.base import Base
from models.rectangle import Rectangle
from inspect import isclass
import unittest
import sys
from io import StringIO


class TestRectangle(unittest.TestCase):
    def setUp(self):
        Base.__nb_objects = 0

    def test_Class(self):
        self.assertTrue(isclass(Rectangle))

    def test_SubClass(self):
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertFalse(issubclass(Base, Rectangle))

    def test_Instance(self):
        r = Rectangle(1, 2)
        self.assertIsInstance(r, Rectangle)
        self.assertIsInstance(r, Base)
        self.assertTrue(type(r) is Rectangle)

    def test_raises(self):

        # TypeError Exception
        with self.assertRaises(TypeError) as err:
            r = Rectangle("string", 5)
        self.assertEqual(str(err.exception), "width must be an integer")

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle(5, "string")
        self.assertEqual(str(err.exception), "height must be an integer")

        with self.assertRaises(TypeError) as err:
            r2 = Rectangle(5, 5, "string")
        self.assertEqual(str(err.exception), "x must be an integer")

        with self.assertRaises(TypeError) as err:
            r3 = Rectangle(5, 5, 5, "string")
        self.assertEqual(str(err.exception), "y must be an integer")

        # ValueError Exception
        with self.assertRaises(ValueError) as err:
            r = Rectangle(-5, 5)
        self.assertEqual(str(err.exception), "width must be > 0")

        with self.assertRaises(ValueError) as err:
            r1 = Rectangle(5, -5)
        self.assertEqual(str(err.exception), "height must be > 0")

        with self.assertRaises(ValueError) as err:
            r = Rectangle(0, 5)
        self.assertEqual(str(err.exception), "width must be > 0")

        with self.assertRaises(ValueError) as err:
            r1 = Rectangle(5, 0)
        self.assertEqual(str(err.exception), "height must be > 0")

        with self.assertRaises(ValueError) as err:
            r2 = Rectangle(5, 5, -5)
        self.assertEqual(str(err.exception), "x must be >= 0")

        with self.assertRaises(ValueError) as err:
            r3 = Rectangle(5, 5, 5, -5)
        self.assertEqual(str(err.exception), "y must be >= 0")

    def test_args(self):
        r_1 = Rectangle(1, 2)
        self.assertEqual(r_1.id, r_1._Base__nb_objects)
        r_2 = Rectangle(1, 2, 3)
        self.assertEqual(r_2.id, r_2._Base__nb_objects)
        r_3 = Rectangle(1, 2, 3, 4, 98)

        self.assertEqual(r_1._Rectangle__width, 1)
        self.assertEqual(r_1._Rectangle__height, 2)
        self.assertEqual(r_1._Rectangle__x, 0)
        self.assertEqual(r_1._Rectangle__y, 0)

        self.assertEqual(r_3._Rectangle__width, 1)
        self.assertEqual(r_3._Rectangle__height, 2)
        self.assertEqual(r_3._Rectangle__x, 3)
        self.assertEqual(r_3._Rectangle__y, 4)
        self.assertEqual(r_3.id, 98)

    def test_setter_getter(self):
        r_1 = Rectangle(1, 2, 3, 4, 98)
        r_1.width = 14
        self.assertEqual(r_1.width, 14)
        r_1.height = 25
        self.assertEqual(r_1.height, 25)
        r_1.x = 10
        self.assertEqual(r_1.x, 10)
        r_1.y = 20
        self.assertEqual(r_1.y, 20)

    def test_area(self):
        r_1 = Rectangle(10, 10)
        self.assertEqual(r_1.area(), 100)

    def test_diplay(self):
        r_1 = Rectangle(2, 3)
        r_2 = Rectangle(4, 2, 0, 3)
        r_3 = Rectangle(3, 4, 3)
        original_stdout = sys.stdout
        output_buffer = StringIO()

        sys.stdout = output_buffer
        r_1.display()
        r_1_got = output_buffer.getvalue()
        sys.stdout = original_stdout

        output_buffer = StringIO()
        sys.stdout = output_buffer
        r_2.display()
        r_2_got = output_buffer.getvalue()
        sys.stdout = original_stdout

        output_buffer = StringIO()
        sys.stdout = output_buffer
        r_3.display()
        r_3_got = output_buffer.getvalue()
        sys.stdout = original_stdout

        self.assertEqual(r_1_got, "##\n##\n##\n")
        self.assertEqual(r_2_got, "\n\n\n####\n####\n")
        self.assertEqual(r_3_got, "   ###\n   ###\n   ###\n   ###\n")

    def test_str(self):
        r = Rectangle(12, 42, 15, 33, 198)
        self.assertEqual(str(r), "[Rectangle] (198) 15/33 - 12/42")

    def test_to_dictionary(self):
        r = Rectangle(12, 42, 15, 33, 198)
        self.assertEqual(r.to_dictionary(), {'x': 15, 'y': 33, 'id': 198,
                                             'height': 42, 'width': 12})


if __name__ == '__main__':
    unittest.main()
