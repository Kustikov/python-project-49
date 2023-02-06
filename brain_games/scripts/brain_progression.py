#!/usr/bin/env python3
from brain_games.start import start_game
from brain_games.games.progression import rules, brain_progression


def main():
    start_game(rules, brain_progression)


if __name__ == "__main__":
    main()
