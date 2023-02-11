#!/usr/bin/env python3
from brain_games.game_core import play_game
from brain_games.games.prime import RULES, brain_prime


def main():
    play_game(RULES, brain_prime)


if __name__ == "__main__":
    main()
