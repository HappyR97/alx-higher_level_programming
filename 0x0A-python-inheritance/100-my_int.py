#!/usr/bin/python3

"""

This module defines MyInt class

"""


class MyInt(int):
    """MyInt subclass"""

    def __eq__(self, other):
        """Returns True is not equal"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Returns True if not equal"""
        return super().__eq__(other)
