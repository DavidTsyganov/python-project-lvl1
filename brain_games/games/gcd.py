import math, random

describer = 'Find the greatest common divisor of given numbers.'


def logic_game():
    number1 = random.randint(1, 99)
    number2 = random.randint(1, 99)
    great_div = math.gcd(number1, number2)
    gmxpr = ('{} {}'.format(number1, number2))
    result = str(great_div)
    return result, gmxpr
    
