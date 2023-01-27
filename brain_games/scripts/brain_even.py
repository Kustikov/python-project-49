#!/usr/bin/env python3
from brain_games.start import start_game, even
from brain_games.games.choose_even import brain_even


def main():
    start_game(even, brain_even)


if __name__ == "__main__":
    main()
