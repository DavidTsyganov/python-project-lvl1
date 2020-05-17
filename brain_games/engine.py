import prompt

ROUNDS = 3


def run(name_game):
    wrong_answer = """'{0}' is wrong answer ;(. Correct answer was '{1}'. Let's try again, {2}!"""
    print("Welcome to the Brain Games!")
    print()
    name = prompt.string('May I have your name?')
    while name == 'yes' or name == 'no' or name == 'No' or name == 'Yes' or name == 'NO' or name == 'nO' or name == 'yES' or name == 'yeS' or name == 'YeS':
        name = prompt.string('Try to input your name correctly')
    print('Hello, {}!'.format(name))
    print()
    print(name_game.DESCRIBER)
    for _try_num in range(0, ROUNDS):
        expression, result = name_game.run_game()
        print('Question:',expression)
        answer = prompt.string('Your answer: ')
        if answer != result:
            print(wrong_answer.format(answer, result, name))
            break
        print('Correct!')
    else:
        print('Congratulations, ',name, '!')
