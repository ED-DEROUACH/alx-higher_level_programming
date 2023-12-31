#!/usr/bin/python3
""" Module that defines the class Student
"""


class Student:
    """Defines a student by first_name, last_name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list of str): A list of attribute names to retrieve.

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        if attrs is None:
            return self.__dict__
        return {key: value for key, value in self.__dict__.items() if key in attrs}
