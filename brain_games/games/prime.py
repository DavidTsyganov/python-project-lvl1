from random import randint 

describer = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return False

    divider = 2
    while divider < number:
        if number % divider == 0:
            return False
        divider += 1
    return True


def logic_game():
    number = randint(1, 1000)
    gmxpr = '{}'.format(number)

    if is_prime(number):
        result = 'yes'
    else:
        result = 'no'

    return result, gmxpr
