#!/usr/bin/env python3
from brain_games.game_core import play_game
from brain_games.games.calculator import RULES, calculator


def main():
    play_game(RULES, calculator)


if __name__ == "__main__":
    main()
