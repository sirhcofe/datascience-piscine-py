class calculator:
    @staticmethod
    def dotproduct(V1, V2):
        """
        Calculate the dot product of two vectors

        Parameters
        ----------
        V1: list[float]
            The first vector
        V2: list[float]
            The second vector
        """
        result = sum(v1 * v2 for v1, v2 in zip(V1, V2))
        print(f"Dor product is: {result}")

    @staticmethod
    def add_vec(V1, V2):
        """
        Calculate the addition of two vectors element-wise

        Parameters
        ----------
        V1: list[float]
            The first vector
        V2: list[float]
            The second vector
        """
        result = [v1 + v2 for v1, v2 in zip(V1, V2)]
        print(f"Add Vector is: {result}")

    @staticmethod
    def sous_vec(V1, V2):
        """
        Calculate the subtraction of two vectors element-wise

        Parameters
        ----------
        V1: list[float]
            The first vector
        V2: list[float]
            The second vector
        """
        result = [v1 - v2 for v1, v2 in zip(V1, V2)]
        print(f"Sous Vector is: {result}")


"""
Static method class do not depend on the internal state of instances of the
class. As such, using staticmethod in this case gives convenience, as it is
not necessary to create an instance of the `calculator` class.
"""
