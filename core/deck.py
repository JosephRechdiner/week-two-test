import random

def build_standard_deck() -> list[dict]:
    special_rank = {1: "A", 11: "J", 12: "Q", 13: "K"}
    result = []
    for i in range(1, 14):
        for suite in ["H", "D", "S", "C"]:
            if i not in special_rank:
                result.append({"rank": str(i), "suite": suite})
            else:
                result.append({"rank": special_rank[i], "suite": suite})
    return result


def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]: 
    for _ in range(swaps):
        # this will indicate if we are good to swap
        good_to_swap = False
        while not good_to_swap:

            # generating 2 indexes
            first_idx = random.randint(0, len(deck) - 1)
            second_idx = random.randint(0, len(deck) - 1)

            # checking if they are not the same index
            not_same_idx = first_idx != second_idx

            # cheking for first card suite match the second index mod
            mod_match = False
            first_card_suite = deck[first_idx]["suite"]
            if (first_card_suite == "H" and second_idx % 5 == 0) or (first_card_suite == "C" and second_idx % 3 == 0) or (first_card_suite == "D" and second_idx % 2 == 0) or (first_card_suite == "S" and second_idx % 7 == 0):
                mod_match = True
            
            # if both are ok breaking out of the loop and swapping
            if not_same_idx and mod_match:
                good_to_swap = True
        # swapping
        deck[first_idx], deck[second_idx] = deck[second_idx], deck[first_idx]
    
    # returning final shuffled deck
    return deck

