from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract base class for characters."""
    def __init__(self, first_name, is_alive=True):
        """
        Initialize a character with a first name and an optional 'is_alive'
        status.

        Parameters
        ----------
        first_name: str
            The first name of the character
        is_alive: bool
            Whether the character is alive (default to True)
        """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """
        Considered as a blueprint for other classes, abstract method is a 
        declaration but does not have an implementation
        """
        pass


class Stark(Character):
    """Class representing a Stark character"""
    def die(self):
        """
        Mark the Stark character as deceased (overrides the method in the
        base class)
        """
        self.is_alive = False
