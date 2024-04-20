#!/usr/bin/python3
"""Contains class MyInt"""


class MyInt(int):
    "Custom int class implimentation"

    def __eq__(self, value):
        """Defines the == operator."""
        return super().__ne__(value)

    def __ne__(self, value):
        """Defines the != operator."""
        return super().__eq__(value)
