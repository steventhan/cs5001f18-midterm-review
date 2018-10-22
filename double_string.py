def double_string_iterative(string):
    ret = ""

    for i in range(len(string)):
        new_letter = string[i] * 2
        ret += new_letter

    return ret


def double_string_recursive(string):
    if not string:
        return ""
    else:
        return string[0] * 2 + double_string_recursive(string[1:])


"""
Write a function to check if a number is in a list
"""

def check_num(lst, num):
    if not lst:
        return False
    else:
        return num == lst[0] or check_num(lst[1:], num)

def check_all_num(lst, num):
    if not lst:
        return False
    elif len(lst) == 1:
        return num == lst[0]    
    else:
        return num == lst[0] and check_all_num(lst[1:], num)