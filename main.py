from core.deck import *
from core.game_logic import *


if __name__ == "__main__":
    new_deck = build_standard_deck()
    shuffled_deck = shuffle_by_suit(new_deck)
    player = {"hand": []}
    dealer = {"hand": []}

    run_full_game(shuffled_deck, player, dealer)