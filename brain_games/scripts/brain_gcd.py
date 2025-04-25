from brain_games.engine import play_game
from brain_games.games.game_nod import RULES, brain_gcd


def main():
    play_game(brain_gcd, RULES)


if __name__ == "__main__":
    main()