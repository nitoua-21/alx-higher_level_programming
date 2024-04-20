"""Module to add a new attribute to an object"""


def add_attribute(obj, name, value):
    """adds a new attribute to an object if it's possible.

    Args:
        obj (object): object
        name (string): attribute's name
        value (Any): attribute's value
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
