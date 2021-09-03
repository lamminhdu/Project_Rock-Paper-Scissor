import random


def is_player_win(human, comp):
    # Check player whether win or not
    if human == 'r' and comp == 's' or human == 'p' and comp == 'r' or human == 's' and comp == 'p':
        return True
    return False


def rock_paper_sicssor():
    # Get computer choice
    comp = random.choice(['r', 'p', 's'])
    type = {'r': 'rock', 'p': 'paper', 's': 'scissor'}
    again = True

    while again:
        player = None
        # Get player choice and check player input
        while player not in ['r', 'p', 's']:
            player = input("\nPlease choose one of these: Rock (r)  ||  Paper (p)  || Scissor (s): ").lower()
            if player not in ['r', 'p', 's']:
                print("Enter wrong!")
        print(f"Player: {type[player]} vs Computer: {type[comp]}")

        # Check winner
        if is_player_win(player, comp):
            res = "Player win!"
        elif comp == player:
            res = "Both tie!"
        else:
            res = "Computer win"

        # Show the result
        print(res)

        # Check whether player want to play again or not
        answer = input("\nDo you want to play again? Yes (y) || No (please type any character): ").lower()
        if answer != 'y':
            again = False

if __name__ == "__main__":
    rock_paper_sicssor()
