#!/usr/bin/python3
""" Square class """


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Square(BaseGeometry):
    """ A Square shape, inherited from BaseGeometry """
    def __init__(self, size):
        """
        Init function for Square

        Attributes:
            size(int): The size of the square
        """
        self.integer_validator("size", size)
        self.__size__ = size

    def __str__(self):
        """
        str function to print width/height

        Returns:
            width or height
        """

        return "[Square] " + str(self.__size__) + "/" + str(self.__size__)

    def area(self):
        """ A function that calculates the area of the Square """
        return self.__size__ ** 2
