# Function to display the board 
def board_display():
    print("       0     1     2")
    print("   --------------------")
    print(f"0  |  {board[0][0]}  |  {board[0][1]}  |  {board[0][2]}  |")
    print("   --------------------")
    print(f"1  |  {board[1][0]}  |  {board[1][1]}  |  {board[1][2]}  |")
    print("   --------------------")
    print(f"2  |  {board[2][0]}  |  {board[2][1]}  |  {board[2][2]}  |")
    print("   --------------------")

#Function to check the Winning status of the match
def win(board):
    for i in range(0,3):
            if((board[i][0]==board[i][1]==board[i][2])and(board[i][0]==board[i][1]==board[i][2]!="  ")):
                return True
            elif((board[0][i]==board[1][i]==board[2][i])and(board[0][i]==board[1][i]==board[2][i]!="  ")):
                return True
    if((board[0][0]==board[1][1]==board[2][2])and(board[0][0]==board[1][1]==board[2][2]!="  ")):
        return True
    elif((board[0][2]==board[1][1]==board[2][0])and(board[0][2]==board[1][1]==board[2][1]!="  ")):
        return True
    else:
        return False

#Function to check the Draw status of the match
def draw(board):
    for row in board:
        if "  " in row:
            return False
    return True
    
    
# Board formation
board = [
    ["  ", "  ", "  "],
    ["  ", "  ", "  "],
    ["  ", "  ", "  "]
]

# Symbol decisions for the players
p1 = input("Enter the symbol for player 1: ")
p2 = input("Enter the symbol for player 2: ")
print("Player 1: " + p1)
print("Player 2: " + p2)

# Input for the players
current_player = p1
while True:
    print(f"\nPlayer {current_player}'s turn")
    row = int(input("Enter the row (0, 1, 2): "))
    col = int(input("Enter the column (0, 1, 2): "))
    if board[row][col] == "  ":
        board[row][col] = current_player
    else:
        print("Invalid entry: The cell is already taken! Try again.")
        continue
    board_display()
    
    # Winning status
    if win(board):
        print(f"Player {current_player} has won the Game")
        break
    
    # Draw status
    elif draw(board):
        print("The game is a draw")
        break
    
    # Switch players
    current_player = p2 if current_player == p1 else p1
