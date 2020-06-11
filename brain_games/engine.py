import prompt

ROUNDS_COUNT = 3


def run(game):
    print("Welcome to the Brain Games!")
    print()
    name = prompt.string('May I have your name?')
    print('Hello, {}!'.format(name))
    print()
    print(game.DESCRIBER)
    for _try_num in range(0, ROUNDS_COUNT):
        expression, result = game.make_data_for_game()
        print('Question:', expression)
        answer = prompt.string('Your answer: ')
        if answer != result:
            print("'{0}' is wrong answer ;(.\
                    Correct answer was '{1}'.".format(answer, result))
            print("Let's try again, {}!".format(name))
            break
        print('Correct!')
    else:
        print('Congratulations, ', name, '!')
