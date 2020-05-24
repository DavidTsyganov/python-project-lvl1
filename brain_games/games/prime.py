import random

DESCRIBER = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    for num in range(2, int(number ** 0.5) + 1):
        if not number % num:
            return False
    return True


def run_game():
    number = random.randint(1, 100)
    expression = str(number)
    result = 'yes' if is_prime(number) else 'no'

    return expression, result
