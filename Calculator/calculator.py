def add(x, y):
    # Edge Cases P P
    #            P N
    #            N N
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y == 0:
        raise ZeroDivisionError('Cannot divide by 0!')

    return x / y
