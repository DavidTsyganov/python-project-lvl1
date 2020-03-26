#!/usr/bin/env python3
from brain_games.games import even
from brain_games.game_engine import game_begin
from brain_games.scripts.brain_games import greet


def main():
    greet()
    game_begin(even)


if __name__ == '__main__':
    main()
