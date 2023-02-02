#!/usr/bin/env python3
from brain_games.start import start_game
from brain_games.games.progression import rules, progression


def main():
    start_game(rules, progression)


if __name__ == "__main__":
    main()
