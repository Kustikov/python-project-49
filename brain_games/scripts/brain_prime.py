#!/usr/bin/env python3
from brain_games.start import start_game, is_prime
from brain_games.games.prime import brain_prime


def main():
    start_game(is_prime, brain_prime)


if __name__ == "__main__":
    main()
