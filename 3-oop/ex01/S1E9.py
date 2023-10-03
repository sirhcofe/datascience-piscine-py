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
        Mark the character as deceased by setting is_alive to False
        """
        self.is_alive = False


class Stark(Character):
    """Class representing a Stark character"""
    def die(self):
        """
        Mark the Stark character as deceased (overrides the method in the
        base class)
        """
        # Call the base class method to set is_alive to False
        super().die()
