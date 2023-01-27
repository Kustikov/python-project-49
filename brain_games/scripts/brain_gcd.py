#!/usr/bin/env python3
from brain_games.start import start_game, nod
from brain_games.games.nod import brain_gcd


def main():
    start_game(nod, brain_gcd)


if __name__ == "__main__":
    main()
