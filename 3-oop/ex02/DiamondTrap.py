from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """
    Class representing a king with properties for eyes and hairs

    Parameters
    ----------
    first_name: str
        The first name of the king
    is_alive: bool, optional
        Whether the king is alive. Defaults to True
    """

    def __init__(sef, first_name, is_alive=True):
        super().__init__(first_name, is_alive)

    # Properties allow getter/setter methods in a way that looks like attribute
    # access, which makes code more readable, for example:
    #   king.set_eyes("blue")
    #   king.eyes = "blue"
    @property
    def eyes(self):
        """The color of the king's eyes"""
        return self._eyes

    @property
    def hairs(self):
        """The color of the king's hair"""
        return self._hairs

    # Using a setter method, it is possible to add data validation logic when
    # settings the value of an attribute
    @eyes.setter
    def eyes(self, value):
        if value.isalpha():
            self._eyes = value
        else:
            raise ValueError("eyes color must be only alphabets")

    @hairs.setter
    def hairs(self, value):
        if value.isalpha():
            self._hairs = value
        else:
            raise ValueError("hair color must be only alphabets")
