#!/usr/bin/env python3
from brain_games.game_core import play_game
from brain_games.games.progression import RULES, brain_progression


def main():
    play_game(RULES, brain_progression)


if __name__ == "__main__":
    main()
