import math, random

DESCRIBER = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    divider = 2
    while number % divider != 0:
        divider += 1
    return divider == number


def run_game():
    number = random.randint(1, 100)
    expression = str(number)
    result = 'yes' if is_prime(number) else 'no'

    return expression, result
