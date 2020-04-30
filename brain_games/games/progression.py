from random import randint

DESCRIBER = 'What number is missing in the progression?'


def run_game():
    number1 = randint(1, 99)
    step = randint(1, 99)
    hidden_number = randint(0, 9)
    counter = 0
    progression = ''
    PROGRESSION_LENGTH = 10

    while counter < PROGRESSION_LENGTH:
        curnumber = number1 + (counter * step)

        if counter == hidden_number:
            element = '.. '
            result = str(curnumber)
        else:
            element = str(curnumber) + " "

        progression += element
        counter += 1

    expression = str(progression)

    return expression, result
