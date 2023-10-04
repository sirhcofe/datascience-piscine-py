import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """
    Represents a student

    Parameters
    ----------
    name: str
        The student's name
    surname: str
        The student's surname
    active: bool, optional
        Indicates whether the student is active. Defaults to True
    login: str
        The student's login name
    id: str
        The student's unique ID

    Note
    ----
    The 'login' and 'id' field are auto-generated and should not explicitly
    provided during initialization.
    """
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    # default_factory allows a function to generates a default value
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self):
        self.login = self.name[0].capitalize() + self.surname.capitalize()


"""
class vs dataclass

A regular Python class is a blueprint for creating objects with attributes and
methods, and user have complete control over how the class behaves, and its
attributes, methods, and initialization logic.

Example:
class MyClass:
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    def method1(self):
        # Method logic here


A dataclass decorator (introduced in 3.7) is designed to simplify the creation
of classes primarily used for storing data. Methods like `__init__`,
`__repr__`, `__eq__`, etc are automatically generated.

Example:
from dataclasses import dataclass

@dataclass
class DataClassExample:
    attribute1: int
    attribute2: str
"""
