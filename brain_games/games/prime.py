import math, random

describer = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    divider = int(math.sqrt(number)) + 1
    for num in range(2, divider):
        if not number % num:
            return False
        return True


def logic_game():
    number = random.randint(1, 1000)
    gmxpr = '{}'.format(number)
    result = 'yes' if is_prime(number) else 'no'

    return result, gmxpr
