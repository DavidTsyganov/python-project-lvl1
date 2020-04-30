from random import randint

DESCRIBER = 'Find the greatest common divisor of given numbers.'


def run_game():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    task = (number1, number2) # keeping numbers to output them later

    while number1 != 0 and number2 != 0:
        if number1 > number2:
            number1 = number1 % number2
        else:
            number2 = number2 % number1

    great_div = number1 + number2
    expression = ('{} {}'.format(task[0], task[1]))
    result = str(great_div)

    return expression, result
    
