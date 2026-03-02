import math

AI = "O"
USER = "X"

def create_board():
    return [["_" for _ in range(3)] for _ in range(3)]

def print_board(board):
    for row in board:
        print("|".join(row))
    print("_" * 9)

def check_win(board, player):
    winning_combinations = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]
    for combo in winning_combinations:
        if all(board[r][c] == player for r, c in combo):
            return True
    return False

def is_full(board):
    return all(board[row][col] != "_" for row in range(3) for col in range(3))

def minimax(board, is_maximizing):
    if check_win(board, AI):
        return 1
    if check_win(board, USER):
        return -1
    if is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == "_":
                    board[row][col] = AI
                    score = minimax(board, False)
                    board[row][col] = "_"
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == "_":
                    board[row][col] = USER
                    score = minimax(board, True)
                    board[row][col] = "_"
                    best_score = min(best_score, score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == "_":
                board[row][col] = AI
                score = minimax(board, False)
                board[row][col] = "_"
                if score > best_score:
                    best_score = score
                    move = (row, col)
    return move

def placing_X(board, row, col):
    if board[row][col] == "_":
        board[row][col] = USER
        return True
    else:
        print("Invalid move. Try again.")
        return False

def main():
    board = create_board()
    turn_count = 0

    print("Welcome to Tic-Tac-Toe!")
    print("Enter your move as 'row,column' (e.g., 0,1).")
    print("You are 'X', AI is 'O'.")
    
    while True:
        print()
        print_board(board)
        print()

        if turn_count % 2 == 0:
            user_input = input("Enter where you want to place: ")
            try:
                row, col = map(int, user_input.split(","))
                if row in [0, 1, 2] and col in [0, 1, 2]:
                    if placing_X(board, row, col):
                        turn_count += 1
                    else:
                        continue
                else:
                    print("Invalid input. Enter row and column between 0 and 2.")
                    continue
            except ValueError:
                print("Invalid input format. Enter as 'row,column'.")
                continue
        else:
            print("AI is making its move...")
            move = best_move(board)
            if move:
                board[move[0]][move[1]] = AI
                turn_count += 1

        if check_win(board, USER):
            print_board(board)
            print("Congratulations! You win!")
            break
        elif check_win(board, AI):
            print_board(board)
            print("AI wins! Better luck next time.")
            break
        elif turn_count == 9:
            print_board(board)
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()