#!/usr/bin/env python3
from brain_games.start import start_game
from brain_games.games.calculator import rules, calculator


def main():
    start_game(rules, calculator)


if __name__ == "__main__":
    main()
