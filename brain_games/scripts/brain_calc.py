from brain_games.engine import play_game
from brain_games.games.game_calc import RULES, calculator


def main():
    play_game(calculator, RULES)


if __name__ == "__main__":
    main()
