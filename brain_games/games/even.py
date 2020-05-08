from random import randint

DESCRIBER = 'Answer "yes" if number even otherwise answer "no".'


def is_even(number):
    return not number % 2


def run_game():
    number = randint(1,99)
    result = 'yes' if is_even(number) else 'no'
    expression = str(number)
    return expression, result
