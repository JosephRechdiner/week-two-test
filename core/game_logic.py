from .player_io import *
import time

def calculate_hand_value(hand :list[dict]) -> int:
    total = 0
    for card in hand:
        if card["rank"] in ["J", "Q", "K"]:
            total += 10
        else:
            total += int(card["rank"]) if card["rank"] != "A" else 1
    return total


def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    # popping 4 cards out of the deck 
    first_player_card, first_dealer_card = deck.pop(), deck.pop()
    second_player_card, secon_dealer_card = deck.pop(), deck.pop()

    # adding all 4 card 2 for each
    player["hand"].append(first_player_card)
    dealer["hand"].append(first_dealer_card)
    
    player["hand"].append(second_player_card)
    dealer["hand"].append(secon_dealer_card)

    # calculating each players hand value
    player_hand_value = calculate_hand_value(player["hand"])
    dealer_hand_value = calculate_hand_value(dealer["hand"])

    # printing total
    print(f"HANDS TOTAL:\nPLAYER: {player_hand_value}\nDEALER: {dealer_hand_value}")
    print("==============================")



def dealer_play(deck: list[dict], dealer: dict) -> bool:
    total = 0
    while total < 17:
        new_card = deck.pop()
        dealer["hand"].append(new_card)
        total = calculate_hand_value(dealer["hand"])

    if total > 21:
        print("DEALER PASSED 21! AND YOU WON THE GAME!\n")
        return False
    
    return True
    

def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    print("==============================")
    print("WELCOME TO BLACKJACK GAME!")
    print("==============================\n")
    print(f"CREATING NEW SHUFFLE DECK...\n")
    time.sleep(1)
    print("DEALING  THE CARDS...\n")
    time.sleep(1)
    deal_two_each(deck, player, dealer)

    while True:
        user_chioce = ask_player_action()
        while user_chioce == "H":    
            cur_card = deck.pop()
            player["hand"].append(cur_card)

            print("YOU CHOOSE TO HIT!")
            print(f"THE CARD YOU GOT IS: {cur_card["rank"]} OF {cur_card["suite"]}\n")

            cur_total = calculate_hand_value(player["hand"])
            if cur_total > 21:
                print("YOU HAVE PASSED 21! YOU LOST THE GAME!\n")
                return None
            
            print(f'NOW YOU GOT: {cur_total} POINTS\n(dealer points: {calculate_hand_value(dealer["hand"])})\n')
            print("==============================")
            user_chioce = ask_player_action()

        player_total = calculate_hand_value(player["hand"])
        dealer_total = calculate_hand_value(dealer["hand"])

        print("YOU CHOOSE TO FINISHED YOU TURN!")
        print("DEALER'S TURN...\n")
        time.sleep(2)
        if dealer_play(deck, dealer):
            
            dealer_total = calculate_hand_value(dealer["hand"])
            if 21 - player_total < 21 - dealer_total:
                print(f"CONGRATS! YOU WON!\nDEALER GOT ONLY {dealer_total} POINTS!\n")
                break
            elif 21 - dealer_total < 21 - player_total:
                print(f"BOOOOO! YOU LOST!\nDEALER GOT {dealer_total} POINTS!\n")
                break
            else:
                print(f"TIE!\nYOU BOTH GOT {dealer_total} POINTS!\n")
                break
        break