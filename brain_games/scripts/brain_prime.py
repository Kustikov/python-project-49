from brain_games.engine import play_game
from brain_games.games.game_prime import RULES, brain_prime


def main():
    play_game(brain_prime, RULES)


if __name__ == "__main__":
    main()