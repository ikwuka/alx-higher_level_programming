#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str):
        result = 0
        numb_convert = 0
        dict_numbers = {"I": 1, "V": 5, "X": 10, "L": 50,
                        "C": 100, "D": 500, "M": 1000}        
        for i in reversed(roman_string):
            numb_convert = dict_numbers[i]
            if result < numb_convert * 5:
                result = result + numb_convert
            else:
                result = result - numb_convert
        return result
    else:
        return 0
