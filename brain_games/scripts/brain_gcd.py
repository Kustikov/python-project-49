#!/usr/bin/env python3
from brain_games.start import start_game
from brain_games.games.nod import rules, brain_gcd


def main():
    start_game(rules, brain_gcd)


if __name__ == "__main__":
    main()
