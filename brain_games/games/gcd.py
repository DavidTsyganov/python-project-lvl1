from random import randint

describer = 'Find the greatest common divisor of given numbers.'


def logic_game():
    number1 = randint(1, 99)
    number2 = randint(1, 99)
    great_div = min(number1, number2)
    gmxpr = ('{} {}'.format(number1, number2))
    while great_div > 0:
        if number1 % great_div == 0 and number2 % great_div == 0:
            result = str(great_div)
            return result, gmxpr
        else: 
            great_div -= 1
