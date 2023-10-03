from S1E9 import Character


class Baratheon(Character):
    """
    Class representing the Baratheon family
    """
    # Set attributes
    family_name = "Baratheon"
    eyes = "brown"
    hairs = "dark"

    def __init__(self, first_name, is_alive=True):
        """
        Initialize a character with a first name and an optional 'is_alive'
        status (overrides the method in the base class)

        Parameters
        ----------
        first_name: str
            The first name of the character
        is_alive: bool
            Whether the character is alive (default to True)
        """
        super().__init__(first_name, is_alive)

    def __str__(self):
        return f"{self.family_name}, {self.eyes}, {self.hairs}"

    def __repr__(self):
        return f"{self.family_name}, {self.eyes}, {self.hairs}"


class Lannister(Character):
    """
    Class representing the Lannister family
    """
    # Set attributes
    family_name = "Lannister"
    eyes = "blue"
    hairs = "light"

    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)

    def __str__(self):
        return f"{self.family_name}, {self.eyes}, {self.hairs}"

    def __repr__(self):
        return f"{self.family_name}, {self.eyes}, {self.hairs}"

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """
        Create a Lannister character using a class method.

        Parameters
        ----------
        first_name: str
            The first name of the character
        is_alive: bool
            Whether the character is alive (default is True)

        Returns
        -------
        Lannister
            A Lannister character
        """
        return cls(first_name, is_alive)
