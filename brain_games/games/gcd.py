from random import randint

describer = 'Find the greatest common divisor of given numbers.'


def logic_game():
    number1 = randint(1, 99)
    number2 = randint(1, 99)
    min_number = min(number1, number2)
    max_number = max(number1, number2)

    devisor = 1
    while devisor <= min_number:
        if min_number % devisor == 0 and max_number % devisor == 0:
            result = str(devisor)
        devisor += 1
    gmxpr = "{} {}".format(number1, number2)
    question = 'Question: ' + gmxpr

    return result, question
