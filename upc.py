
def check_upc(string):
    rev = string[::-1]
    sum_odd = 0
    sum_even = 0

    for i in range(len(rev)):
        if i % 2 == 0:
            sum_even += rev[i]
        if i % 2 == 1:
            sum_odd += rev[i] * 3
    
    total = sum_even + sum_odd
    # if total % 10 == 0:
    #     return True
    # else:
    #     return False
    
    return total % 10 == 0
    
