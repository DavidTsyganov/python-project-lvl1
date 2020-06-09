from random import randint, choice

DESCRIBER = 'What number is missing in the progression?'
PROGRESSION_LENGTH = 10


def make_data_for_game():
    start_number = randint(1, 99)
    step = randint(1, 99)
    maximum_number = (step * PROGRESSION_LENGTH) + start_number
    progression_index = range(start_number, maximum_number, step)
    result = choice(progression_index)
    progression = ' '.join([
'..' if num == result else str(num) for num in progression_index])
    expression = f'{progression}'
    return expression, result
