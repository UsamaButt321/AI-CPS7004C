board = [[" " for _ in range(3)] for _ in range(3)]

def print_board():
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(player):
    for row in board:
        if all([cell == player for cell in row]):
            return True

    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False

def main():
    player = "X"
    while True:
        print_board()
        try:
            row, col = map(int, input(f"Player {player}, enter your move (row and column, separated by a space): ").split())
            if board[row - 1][col - 1] != " ":
                raise ValueError("Invalid move. Space already occupied.")

            board[row - 1][col - 1] = player
            if check_win(player):
                print_board()
                print(f"Player {player} wins!")
                break

            if any([" " in row for row in board]):
                player = "O" if player == "X" else "X"
            else:
                print_board()
                print("It's a draw!")
                break

        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()