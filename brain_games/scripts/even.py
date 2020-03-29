from random import randint

describer= 'Answer "yes" if number even otherwise answer "no".'


def even_game():
    count1 = randint(1,100)

    if count1 % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'

    gmxpr = '{}'.format(count1)

    return answer, gmxpr, count1
