import math

class Vector2D(object):
    """
    A class representing a 2D vector with basic vector operations.

    Attributes:
        x (float): The x-coordinate of the vector.
        y (float): The y-coordinate of the vector.
        thresh (float): A small threshold used for floating-point comparison to determine vector equality.
    """

    def __init__(self, x=0, y=0):
        """
        Initializes a new instance of Vector2D.

        Args:
            x (float, optional): The x-coordinate of the vector. Defaults to 0.
            y (float, optional): The y-coordinate of the vector. Defaults to 0.
        """
        self.x = x
        self.y = y
        self.thresh = 0.000001

    def __add__(self, other):
        """
        Adds two vectors.

        Args:
            other (Vector2D): The vector to add to the current vector.

        Returns:
            Vector2D: A new Vector2D instance representing the sum of the two vectors.
        """
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """
        Subtracts one vector from another.

        Args:
            other (Vector2D): The vector to subtract from the current vector.

        Returns:
            Vector2D: A new Vector2D instance representing the difference between the two vectors.
        """
        return Vector2D(self.x - other.x, self.y - other.y)

    def __neg__(self):
        """
        Negates the vector.

        Returns:
            Vector2D: A new Vector2D instance representing the negation of the current vector.
        """
        return Vector2D(-self.x, -self.y)

    def __mul__(self, scalar):
        """
        Scales the vector by a scalar.

        Args:
            scalar (float): The scalar value to multiply the vector by.

        Returns:
            Vector2D: A new Vector2D instance representing the scaled vector.
        """
        return Vector2D(self.x * scalar, self.y * scalar)

    def __div__(self, scalar):
        """
        Divides the vector by a scalar. This method is used for Python 2.x compatibility.

        Args:
            scalar (float): The scalar value to divide the vector by.

        Returns:
            Vector2D or None: A new Vector2D instance representing the divided vector, or None if the scalar is zero.
        """
        if scalar != 0:
            return Vector2D(self.x / float(scalar), self.y / float(scalar))
        return None

    def __truediv__(self, scalar):
        """
        Divides the vector by a scalar. This method is used for Python 3.x compatibility.

        Args:
            scalar (float): The scalar value to divide the vector by.

        Returns:
            Vector2D: A new Vector2D instance representing the divided vector.
        """
        return self.__div__(scalar)
    
    def __eq__(self, other):
        """
        Checks if two vectors are equal.

        Args:
            other (Vector2D): The vector to compare with the current vector.

        Returns:
            bool: True if the vectors are equal within the defined threshold, False otherwise.
        """
        if abs(self.x - other.x) < self.thresh:
            if abs(self.y - other.y) < self.thresh:
                return True
        return False
    
    def magnitudeSquared(self):
        """
        Computes the squared magnitude of the vector.

        Returns:
            float: The squared magnitude of the vector.
        """
        return self.x**2 + self.y**2

    def magnitude(self):
        """
        Computes the magnitude (length) of the vector.

        Returns:
            float: The magnitude of the vector.
        """
        return math.sqrt(self.magnitudeSquared())

    def copy(self):
        """
        Creates a copy of the current vector.

        Returns:
            Vector2D: A new Vector2D instance with the same coordinates as the current vector.
        """
        return Vector2D(self.x, self.y)

    def asTuple(self):
        """
        Converts the vector to a tuple.

        Returns:
            tuple: A tuple representing the coordinates of the vector (x, y).
        """
        return self.x, self.y

    def asInt(self):
        """
        Converts the vector's coordinates to integers.

        Returns:
            tuple: A tuple of integers representing the coordinates of the vector (x, y).
        """
        return int(self.x), int(self.y)

    def __str__(self):
        """
        Provides a string representation of the vector.

        Returns:
            str: A string representing the vector in the format "<x, y>".
        """
        return "<" + str(self.x) + ", " + str(self.y) + ">"
