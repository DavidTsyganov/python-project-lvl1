#!/usr/bin/env python3
from brain_games.scripts.brain_games import greet
from brain_games.game_engine import start_game
from brain_games.games import calc


def main():
    greet()
    start_game(calc)


if __name__ == '__main__':
    main()
