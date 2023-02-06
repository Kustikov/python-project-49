#!/usr/bin/env python3
from brain_games.start import start_game
from brain_games.games.even import rules, brain_even


def main():
    start_game(rules, brain_even)


if __name__ == "__main__":
    main()
