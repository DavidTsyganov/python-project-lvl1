#! /usr/bin/env python3
import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    print()
    name = prompt.string('May I have your name?')
    print('Hello, {}!'.format(name))
    print()
    return name


def start_game(name_game):
    print(name_game.describer)
    counter = 0
    name = welcome_user()

    while counter != 3:
        result,gmxpr = name_game.logic_game()
        question = 'Question :' + gmxpr

        print(question)
        response = prompt.string('Your answer: ')

        if response == result:
            print('Correct!')
            counter += 1 
            if counter == 3:
                print("Congratulations, {}!".format(name))

        else:
            error_output = "'{}' is wrong answer :(. ".format(response)
            correct_output = "Correct answer was '{}'.".format(result)
            print(error_output + correct_output)
            print("Let's try again, {}!".format(name))
            counter += 3
