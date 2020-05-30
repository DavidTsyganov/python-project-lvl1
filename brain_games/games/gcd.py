from random import randint

DESCRIBER = 'Find the greatest common divisor of given numbers.'


def gcd(number1, number2):
    while number1 != 0 and number2 != 0:
        if number1 > number2:
            number1 = number1 % number2
        else:
            number2 = number2 % number1
    return number1 + number2


def make_data_for_game():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    expression = ('{} {}'.format(number1, number2))
    result = str(gcd(number1, number2))
    return expression, result
