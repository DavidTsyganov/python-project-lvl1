from random import randint

describer = 'Answer "yes" if number even otherwise answer "no".'


def logic_game():
    count1 = randint(1, 99)

    if count1 % 2 == 0:
        result = 'yes'
    else:
        result = 'no'

    gmxpr = '{}'.format(count1)

    return result,gmxpr
