import random

squares = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def game_board(squares):
    print(f"\n  ------------------\n |  {squares[0]}  |  {squares[1]}  |  {squares[2]}  |\n |     |     |     |\n  ------------------\n |  {squares[3]}  |  {squares[4]}  |  {squares[5]}  |\n |     |     |     |\n  ------------------\n |  {squares[6]}  |  {squares[7]}  |  {squares[8]}  |\n |     |     |     |\n  ------------------")

def someone_win(squares):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for condition in win_conditions:
        if all(squares[i] == "X" for i in condition):
            game_board(squares)
            print("You win!")
            return True
        elif all(squares[i] == "O" for i in condition):
            game_board(squares)
            print("You lose!")
            return True
    if "1" not in squares and "2" not in squares and "3" not in squares and "4" not in squares and "5" not in squares and "6" not in squares and "7" not in squares and "8" not in squares and "9" not in squares:
        print("It's a tie!")
        return True
    return False

game_on = True

while game_on:
    game_board(squares)
    user_choice = input("choose a number in squares:")
    if user_choice not in squares:
        user_choice = input("The number doesn't exist in the boar. Please try again with a number in the board:")
    index_to_replace = squares.index(user_choice)
    squares[index_to_replace] = "X"
    if someone_win(squares):
        game_on = False
        break

    while game_on:
        machine_random_sq_index = random.randint(0, 8)
        if squares[machine_random_sq_index] not in ["X", "O"]:
            squares[machine_random_sq_index] = "O"
            if someone_win(squares):
                game_on = False
            break
