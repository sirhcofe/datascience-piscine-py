class calculator:
    def __init__(self, vector):
        self.vector = vector

    def __add__(self, scalar):
        self.vector = [x + scalar for x in self.vector]
        print(self.vector)

    def __mul__(self, scalar):
        self.vector = [x * scalar for x in self.vector]
        print(self.vector)

    def __sub__(self, scalar):
        self.vector = [x - scalar for x in self.vector]
        print(self.vector)

    def __truediv__(self, scalar):
        if scalar == 0:
            raise ValueError("division by zero is not allowed.")
        self.vector = [x / scalar for x in self.vector]
        print(self.vector)
