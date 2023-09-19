def fizzbuzz(value):
    if isdivisible(value, 3):
        if isdivisible(value, 5):
            return 'FizzBuzz'
        return 'Fizz'
    if isdivisible(value, 5):
        return 'Buzz'
    return str(value)

def isdivisible(value, mod):
    return (value % mod) == 0