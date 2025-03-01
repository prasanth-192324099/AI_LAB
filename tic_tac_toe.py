
board = [" " for _ in range(9)]

def print_board():
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("--+---+--")

def check_winner(player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8], 
        [0, 4, 8], [2, 4, 6]              
    ]
    return any(all(board[i] == player for i in combo) for combo in winning_combinations)

def check_draw():
    return " " not in board

def tic_tac_toe():
    current_player = "X"
    
    while True:
        print_board()
        try:
            move = int(input(f"Player {current_player}, enter a position (1-9): ")) - 1
            if board[move] == " ":
                board[move] = current_player
            else:
                print("Position already taken. Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Choose a number between 1 and 9.")
            continue
        
        if check_winner(current_player):
            print_board()
            print(f"Player {current_player} wins!")
            break
        
        if check_draw():
            print_board()
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

tic_tac_toe()
