import math, random

DESCRIBER = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number % 2 == 0:
        return number == 2
    d = 3
    while d ** 2 <= number and number % d != 0:
        d += 2 
    return d ** 2 > number


def run_game():
    number = random.randint(1, 100)
    expression = str(number)
    result = 'yes' if is_prime(number) else 'no'

    return expression, result
