from random import randint

describer = 'Answer "yes" if number even otherwise answer "no".'

def is_even(number):
    return not number % 2

def run_game():
    quest = randint(1,99)
    result = 'yes' if is_even(quest) else 'no'
    expression = ' {}'.format(quest)
    return expression, result
