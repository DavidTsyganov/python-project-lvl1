import random, operator

DESCRIBER = 'What is the result of the expression?'

OPERATIONS = (
        ('+', operator.add),
        ('-', operator.sub),
        ('*', operator.mul),
    )
def run_game():
    operation_sign, operation = random.choice(OPERATIONS)
    number1 = random.randint(1, 99)
    number2 = random.randint(1,99)
    result = str(operation(number1, number2))
    expression = '{0} {1} {2}'.format(number1, operation_sign, number2)
    return expression, result


