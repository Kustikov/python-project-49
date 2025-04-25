from brain_games.engine import play_game
from brain_games.games.game_progression import RULES, brain_progression


def main():
    play_game(brain_progression, RULES)


if __name__ == "__main__":
    main()