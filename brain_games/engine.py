#!/usr/bin/env python3

import prompt


wrong_answer = """'{0}' is wrong answer ;(. Correct answer was '{1}'. Let's try again, {2}!"""

def welcome_user():
        print("Welcome to the Brain Games!")
        print()
        name = prompt.string('May I have your name?')
        print('Hello, {}!'.format(name))
        print()
        return name

def run(name_game):
    name = welcome_user()
    print(name_game.describer)

    for _try_num in range(0,3):
        gmxpr, result = name_game.logic_game()
        print('Question: {gmxpr}'.format(gmxpr=gmxpr))
        answer = prompt.string('Your answer: ')

        if answer != result:
            print(wrong_answer.format(answer, result, name))
            break
        print('Correct!')
    else:
        print('Congratulations, {name}!'.format(name=name))
