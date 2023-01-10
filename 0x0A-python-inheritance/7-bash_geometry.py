#!/usr/bin/python3
""" BaseGeometry class """


class BaseGeometry:
    """ Represent BaseGeometry """
    
    def area(self):
        """ Yet to be implemented """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        Validate a parameter as an integer
        
        Args:
            name(str): The name of the parameter.
            value(int): The parameter to be validated
            
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        