import math, random

describer = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    prime = number - 1
    while number % prime != 0:
        prime -= 1
    if prime == 1:
        return True
    return False

def logic_game():
    number = random.randint(1, 100)
    expression = '{}'.format(number)
    result = 'yes' if is_prime(number) else 'no'

    return expression, result
