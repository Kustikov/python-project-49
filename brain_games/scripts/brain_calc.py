#!/usr/bin/env python3
from brain_games.game_core import play_game
from brain_games.games.calculator import print_rules, calculator


def main():
    play_game(print_rules, calculator)


if __name__ == "__main__":
    main()
