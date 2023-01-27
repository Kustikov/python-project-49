#!/usr/bin/env python3
from brain_games.start import start_game, calc
from brain_games.games.calculator import calculator


def main():
    start_game(calc, calculator)


if __name__ == "__main__":
    main()
