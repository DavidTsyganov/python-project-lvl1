from random import randint, choice

describer = 'What is the result of the expression?'


def logic_game():
    number1 = randint(1, 99)
    number2 = randint(1,99)
    doing = choice('+-*')

    if doing == '+':
        result = str(number1 + number2)
    elif doing == '-':
        if number1 < number2:
            result = str(number2 - number1)
        else:
            result = str(number1 - number2)
    else:
        result = str(number1 * number2)

    gmxpr = str(number1) + " {} ".format(doing) + str(number2)

    return result, gmxpr
