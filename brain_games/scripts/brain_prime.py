#!/usr/bin/env python3
from brain_games.start import start_game
from brain_games.games.prime import rules, brain_prime


def main():
    start_game(rules, brain_prime)


if __name__ == "__main__":
    main()
