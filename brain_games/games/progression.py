from random import randint

DESCRIBER = 'What number is missing in the progression?'
PROGRESSION_LENGTH = 10


def make_data_for_game():
    number1 = randint(1, 99)
    step = randint(1, 99)
    counter = 0
    question = ''
    hidden_number = randint(0, PROGRESSION_LENGTH - 1)
    while counter < PROGRESSION_LENGTH:
        current_number = number1 + (counter * step)
        if counter == hidden_number:
            element = '.. '
            result = str(current_number)
        else:
            element = str(current_number) + " "
        question += element
        counter += 1
    expression = str(question)
    return expression, result
