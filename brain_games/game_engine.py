import brain_games.games.cli
import prompt


def start_game(name_game):
    print(name_game.describer)
    counter = 1
    name = brain_games.games.cli.welcome_user()

    while counter <= 3:
        result,gmxpr = name_game.logic_game()
        question = 'Question :' + gmxpr

        print(question)
        response = prompt.string('Your answer: ')

        if response == result:
            print('Correct!')
            counter += 1 
            if counter > 3:
                print("Congratulations, {}!".format(name))

        else:
            error_output = "'{}' is wrong answer :(. ".format(response)
            correct_output = "Correct answer was '{}'.".format(result)
            print(error_output + correct_output)
            print("Let's try again, {}!".format(name))
            counter += 3
