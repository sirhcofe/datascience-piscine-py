from S1E9 import Character


class Baratheon(Character):
    """
    Class representing the Baratheon family
    """

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
        # Set attributes
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"

    def __repr__(self):
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"

    def die(self):
        super().die()


class Lannister(Character):
    """
    Class representing the Lannister family
    """

    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        # Set attributes
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"

    def __repr__(self):
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"

    def die(self):
        super().die()

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
