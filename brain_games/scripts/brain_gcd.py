#!/usr/bin/env python3
from brain_games.game_core import play_game
from brain_games.games.nod import print_rules, brain_gcd


def main():
    play_game(print_rules, brain_gcd)


if __name__ == "__main__":
    main()
