import prompt

roundsCount = 3


def run(game):
    #wrong_answer = """'{0}' is wrong answer ;(. Correct answer was '{1}'.\n
#Let's try again, {2}!"""
    print("Welcome to the Brain Games!")
    print()
    name = prompt.string('May I have your name?')
    print('Hello, {}!'.format(name))
    print()
    print(game.DESCRIBER)
    for _try_num in range(0, roundsCount):
        expression, result = game.make_data_for_game()
        print('Question:', expression)
        answer = prompt.string('Your answer: ')
        if answer != result:
            print("""'{0}' is wrong answer ;(. Correct answer was '{1}'.\n
Let's try again, {2}!""".format(answer, result, name))
            break
        print('Correct!')
    else:
        print('Congratulations, ', name, '!')
