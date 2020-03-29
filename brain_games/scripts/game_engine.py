import cli
import prompt
rounds = 3


def game_begin():
    greetings = 'Welcome to the Brain games!'
    print(greetings)
    print(game_name.describer)
    name = brain_games.cli.welcome_user()

    counter = 1
    while counter <= rounds:
        answer , gmxpr = game_name.logic_game()
        question = 'Question: ' + gmxpr

        print(question)
        rspons = prompt.string('Your answer: ')

        if rspons == answer:
            if counter == rounds:
                print('Correct!')
                print("Congratulations, {}!".format(name))
                break
            else:
                print('Correct!')
                counter += 1

        else:
            error_output = "'{}' is wrong answer ;(. ".format(rspons)
            correct_output = "Correct answer was '{}'.".format(answer)
            print(error_output + correct_output)
            print("Let's try again, {}!".format(name))
