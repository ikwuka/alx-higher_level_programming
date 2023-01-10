#!/usr/bin/python3
""" Rectangle subclass """

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle that inherits from BaseGeometry """
    def __init__(self, width, height):
        BaseGeometry.integer_validator(self, "height", height)
        self.__height__ = height
        BaseGeometry.integer_validator(self, "width", width)
        self.__width__ = width

    def area(self):
        return self.__width__ * self.__height__

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width__, self.__height__)
