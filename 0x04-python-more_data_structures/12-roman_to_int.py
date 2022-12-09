#!/usr/bin/python3
def roman_to_int(roman_string):
    
    dict_numbers = {"I": 1, "V": 5, "X": 10, "L": 50, \
                    "C": 100, "D": 500, "M": 1000, "IV": 4, \
                    "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900
                    }
    
    if roman_string and type(roman_string) == str:
        num = 0
        for i in range(len(roman_string)):
            for j in dict_numbers.keys():
                if roman_string[:] is j:
                    num = dict_numbers[j]
                    return num
                if roman_string[i:i+1] is j:
                    num += dict_numbers[j]
                    break
                
        return num
    else:
        return 0
