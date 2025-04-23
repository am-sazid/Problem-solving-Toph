def make_negative( number ):
    if number > 0:
        return -number
    else:
        return number
print(make_negative(5))  # Output: -5

def make_negative( number ):
    return -abs(number)
print(make_negative(5))  # Output: -5