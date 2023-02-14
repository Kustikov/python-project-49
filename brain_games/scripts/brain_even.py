#!/usr/bin/env python3
from brain_games.game_core import play_game
from brain_games.games.even import RULES, brain_even


def main():
    play_game(RULES, brain_even)


if __name__ == "__main__":
    main()
