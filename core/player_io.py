def ask_player_action() -> str:
    while True:
        user_input = input("ENTER H: HIT OR S: STAND: ")
        print("==============================")
        if len(user_input) > 1:
            print("YOU MUST ENTER ONE LETTER ONLY H OR S\n")
        if user_input == "H" or user_input == "S" or user_input == "h" or user_input == "s":
            return user_input.upper()

        print("YOU MUST ENTER H OR S\n")




