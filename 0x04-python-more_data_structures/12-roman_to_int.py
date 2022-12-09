#!/usr/bin/python3
def roman_to_int(roman_string):
    # @roman_string - returns the roman numeral of an integer
    if isinstance(roman_string, str):
        result = 0
        numb_convert = 0
        dict_nums = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, \
                      "M": 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900 }
        for i in reversed(roman_string):
            numb_convert = dict_nums[i]
            if result < numb_convert * 5:
                result = result + numb_convert
            else:
                result = result - numb_convert
        return result
    else:
        return 0
