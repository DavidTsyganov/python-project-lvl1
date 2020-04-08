import random, operator

describer = 'What is the result of the expression?'

operators = (
        ('+', operator.add),
        ('-', operator.sub),
        ('*', operator.mul),
    )
def logic_game():
    symbol, operation = random.choice(operators)
    number1 = random.randint(1, 99)
    number2 = random.randint(1,99)
    result = str(operation(number1, number2))
    gmxpr = '{0} {1} {2}'.format(number1, symbol, number2)
    return gmxpr, result
