#!/usr/bin/python3
"""Square module"""

class Square:
    """Define square"""

    def __init__(self, size=0):
        """Constructor

        Args:
            size: length of square's size
        """
        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Properties for the size of square
        
        Raise:
            TypeError: if size is not an integer
            ValueError: if size <0
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter function for private attribute size
        Args:
            value: value to be set
        Returns:
            nothing
        """
        if not (isinstance(value, int)):
            raise TypeError("size must be >= 0")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        
    def area(self):
        """Area of the square.
        Returns:
            the size of square
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square"""
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="\n" if j is self.size - 1 and i != j else "")
            print()
