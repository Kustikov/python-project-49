from brain_games.engine import play_game
from brain_games.games.game_even import RULES, brain_even


def main():
    play_game(brain_even, RULES)


if __name__ == "__main__":
    main()
