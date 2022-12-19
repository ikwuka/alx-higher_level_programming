#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list_div = []
    total = 0
    for index in range(list_length):
        try:
            total = my_list_1[index] / my_list_2[index]
        except ZeroDivisionError:
            total = 0
            print("division by 0")
        except TypeError:
            total = 0
            print("wrong type")
        except IndexError:
            total = 0
            print("out of range")
        finally:
            new_list_div.append(total)
    return new_list_div
