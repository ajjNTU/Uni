# my notes:
# using 1-9 just to complicate things but maybe cause it's more intuitive
# for a user?
# 2nd only wins with 1st making a mistake else chases tie


#
# idea: have it store mistakes and at end of game reveal them
#       wagers??? :)
#
# display the game instructions
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
turn = 1
human = " "
computer = " "
mistake1 = 0
mistake2 = 0
end = 0


def display_instructions():
    print(
"""
Learn to Tic-Tac-Toe
This game is solved and I will help you
too to solve it. 
Or maybe you already did?
I will only play perfectly, sorry.
Once the game is solved it will end
But I will try and help you along the way
Our Board
     |     |
  1  |  2  |  3
_____|_____|_____ 
     |     |
  4  |  5  |  6
_____|_____|_____   
     |     |
  7  |  8  |  9
     |     |
""")
# display_instructions()


# determine who goes first
def ask_yes_no(question):
    answer = ""
    while not (answer == "y" or answer == "n"):
        answer = input(question)
    return answer


def pieces():
    global human
    global computer

    want_first = ask_yes_no("Would you like to go 1st? Enter y or n: ")
    if want_first == "y":
        print("Wise Choice. You will be 'X'cellent")
        human = "X"
        computer = "O"
    else:
        print("Bold Strategy Cotton. Let's see if it pays off. You will be 'O'")
        human = "O"
        computer = "X"


# pieces()


def new_board():
    global board
    global turn
    global mistake1
    global mistake2
    # wipe it clean?
    # index   0    1    2    3    4    5    6    7    8
    #         1    2    3    4    5    6    7    8    9
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    turn = 1
    mistake2 = 0
    mistake1 = 0

#new_board()
#print(board)

""" create an empty tic-tac-toe board
# display the board """
def display_board(board):
    one = board[0]
    two = board[1]
    three = board[2]
    four = board[3]
    five = board[4]
    six = board[5]
    seven = board[6]
    eight = board[7]
    nine = board[8]
    print(f"""
     |     |
  {one}  |  {two}  |  {three}
_____|_____|_____ 
     |     |
  {four}  |  {five}  |  {six}
_____|_____|_____   
     |     |
  {seven}  |  {eight}  |  {nine}
     |     |
    """)


# display_board(board)
#
# # index   0    1    2    3    4    5    6    7    8
# #         1    2    3    4    5    6    7    8    9
# board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]


def legal_moves(board):
    legal_moves = []
    for index, square in enumerate(board):
        if square == " ":
            legal_moves.append(index+1)
    #print(legal_moves)
    return legal_moves


# legal_moves(board)
# display_board(board)
# board = [" " , " ", " ", " ", "X", "O", "O", "O", "X"]
# display_board(board)


# winnings trios (1,2,3) (4,5,6) (7,8,9) (1,4,7) (2,5,8) (3,6,9) (1,5,9) (3,5,7)
def winner(board):
    global end

    crosses = []
    noughts = []
    crosses_win = False
    noughts_win = False
    end = 0
    winning_trio = [[1, 2, 3],[4, 5, 6],[7, 8, 9],[1, 4, 7],[2, 5, 8],[3, 6, 9],[1, 5, 9],[3, 5, 7]]
    for index, square in enumerate(board):
        if square == "X":
            crosses.append(index+1)
            #print("c",crosses)
        if square == "O":
            noughts.append(index+1)
            #print(f"n: {noughts}")
    for winners in winning_trio:
        set_winner = set(winners)
        set_crosses = set(crosses)
        set_noughts = set(noughts)
        if set_winner.intersection(set_crosses) == set_winner:
            crosses_win = True
        if set_winner.intersection(set_noughts) == set_winner:
            noughts_win = True
    if noughts_win is True:
        print("O wins, WOW")
        end = 1
        return "0"
    elif crosses_win is True:
        print("X wins, nothing special here")
        end = 1
        return "X"
    # how do i define a TIE, no legal moves and none above. probably a better way cause I'd like to call a TIE before
    # having to place all the pieces
    elif legal_moves(board) == []:
        end = 1
        print("TIE right?")
    else:
        return None


# winner(board)
def winner_check(board):
    crosses = []
    noughts = []
    winning_trio = [[1, 2, 3],[4, 5, 6],[7, 8, 9],[1, 4, 7],[2, 5, 8],[3, 6, 9],[1, 5, 9],[3, 5, 7]]
    for index, square in enumerate(board):
        if square == "X":
            crosses.append(index+1)
            #print("c",crosses)
        if square == "O":
            noughts.append(index+1)
            #print(f"n: {noughts}")
    for win_check in winning_trio:
        set_winner = set(win_check)
        set_crosses = set(crosses)
        set_noughts = set(noughts)
        if len(set_crosses.intersection(set_winner)) == 2 and len(set_noughts.intersection(set_winner)) == 0:
            winning_square = int(list(set_winner.difference(set_crosses))[0])
            return winning_square


def O_winner_check(board):
    crosses = []
    noughts = []
    winning_trio = [[1, 2, 3],[4, 5, 6],[7, 8, 9],[1, 4, 7],[2, 5, 8],[3, 6, 9],[1, 5, 9],[3, 5, 7]]
    for index, square in enumerate(board):
        if square == "X":
            crosses.append(index+1)
            #print("c",crosses)
        if square == "O":
            noughts.append(index+1)
            #print(f"n: {noughts}")
    for win_check in winning_trio:
        set_winner = set(win_check)
        set_crosses = set(crosses)
        set_noughts = set(noughts)
        if len(set_noughts.intersection(set_winner)) == 2 and len(set_crosses.intersection(set_winner)) == 0:
            o_winning_square = int(list(set_winner.difference(set_crosses))[0])
            return o_winning_square

# while nobody’s won and it’s not a tie
#     if it’s the human’s turn
def human_move(board, human):
    # what's your move, variable board and human where human is the humans piece X/O
    global turn

    ok_move = 0
    print(f"Turn #: {turn}")
    while ok_move == 0:
        legals = list(legal_moves(board))
        # print("legals", legals)
        h_move = input(f"Enter square from {legals}: ")
        try:
            h_move = int(h_move)
        except ValueError:
            print(f"{h_move} is not a number, you can chose from {legals}")
        else:
            if h_move in legals:
                ok_move = 1
            else:
                print(f"{h_move} is not a legal square, you can chose from {legals}")
    board[h_move-1] = human
    turn += 1

# print(board)
# human_move(board, human)
# print(board)

#           get the human’s move
#           update the board with the move
#     otherwise
#           calculate the computer’s move

# computer first perfect mode
#
# available moves [1,..9]
# best 1st move corner? lets chose nine
#  available moves [1,..8]
# 2nd:
#   middle = tie or win
#   #  available moves [1,2,3,4,6,7,8]
#       3rd move = 1
#       available moves [2,3,4,6,7,8]
#       if 4th move side not corner [2,4,6,8] then always tie cause chasing 3ofkind
#       if 4th move corner [3,7]
#           pick opposite corner to there pick
#           so if 3 then 7 if 7 then 3
#   non middle = win
#        3rd move if 1st was 9: nonmiddle (1,4,3,6) = 7, (7, 8, 2) = 3
#          generalise this?
#        4th move has to stop current possible win
#         5th move: 9 then 7 = 1 if 1 not possible then 3
#           declare victory 2ndPlayer can't win
#
#
# computer 2nd mode:
#      chase tie if no mistake (user follows solve above)
#           if user makes a mistake can we win? and lets do that
# new_board()


def computer_move(board, computer, human):
    # would it be smarter to use?
    # i think placing the pieces could be a function and maybe check it's writing to a blank? and print the move
    # move stuff
    # 1st move is ours (probably rarer), they'll want to try and win so lets assume they play perfect
    global turn
    global mistake1
    global mistake2

    if turn != 1 and computer != "O":
        print(f"Turn #: {turn}")
    if turn == 1 and computer == "X":
        board[8] = "X"
        print("I picked 9")
        turn += 1
    if turn == 3 and computer == "X" and board[4] == "O":
        # perfect 2nd move play, go opposite our start
        board[0] = "X"
        print("I picked 1")
        turn +=1
    if turn == 3 and computer == "X":
        # mistake? non middle algo to victory
        if board.index("O") in [0,1,3,2,5]:
            board[6] = "X"
            print("I picked 7")
            turn += 1
        else:
            board[2] = "X"
            print("I picked 3")
            turn += 1
        mistake1 = 1
    if turn == 5 and computer == "X" and mistake1 == 1:
        if board[6] == "X":
            if board[7] != "O":
                board[7] = "X"
                print("I picked 8")
            else:
                if board[3] == "O" or board[0] == "O":
                    board[2] = "X"
                    print("I picked 3")
                    turn += 1
                elif board[1] == "O":
                    board[4] = "X"
                    print("I picked 5")
                    turn += 1
                else:
                    board[0] = "X"
                    print("I picked 1")
                    turn += 1
        elif board[2] == "X":
            if board[5] != "O":
                board[5] = "X"
                print("I picked 6")
            else:
                board[0] = "X"
                print("I picked 1")
                turn += 1
    elif turn == 5 and computer == "X" and (board[1] == "O" or board[3] == "O" or board[5] == "O" or board[7] == "O"):
        # this should continue the perfect play to end in a tie
        # defend the tie
        # we could use a O_win_check function and place their winning space
        block_index = O_winner_check(board) - 1
        board[block_index] = "X"
        print(f"I picked {block_index}")
        turn += 1
    elif turn == 5 and computer == "X" and mistake1 == 0:
        # mistake? algo to victory, they went corner 3 or 7
        if board[2] == "O":
            board[6] = "X"
            print("I picked 7")
            turn += 1
        if board[6] == "O":
            board[2] = "X"
            print("I picked 3")
            turn += 1
        mistake2 = 1
    if turn == 7 and mistake2 == 0 and mistake1 == 0:
        block_index = O_winner_check(board) - 1
        board[block_index] = "X"
        print(f"I picked {block_index}")
        turn += 1
    if turn == 7 and mistake1 == 1:
        # finishing win on mistake1
        win_index = winner_check(board) - 1
        board[win_index] = "X"
        print(f"I picked {win_index}")
    if turn == 7 and mistake2 == 1:
        win_index = winner_check(board) - 1
        board[win_index] = "X"
        print(f"I picked {win_index}")
    if turn == 9 and mistake2 == 0 and mistake1 == 0:
        block_index = O_winner_check(board) - 1
        board[block_index] = "X"
        print(f"I picked {block_index}")
        turn += 1
    #time to decide what to do with 2nd player
    if computer == "O":
        if turn == 2 and board.index("X") in [0,2,6,8]:
            board[4] = "O"
            turn += 1
        elif turn == 2:
            # mistake 3? they didn't go a corner so lets try and win?
            board[8] = "O"
            turn += 1
        elif turn == 4 and (board[0] == "X" and board [8] == "X") or (board[2] == "X" and board [6] == "X"):
            # if they picked perfect game and chose opposite to start
            board[1] = "O"
            turn += 1
        elif turn == 4:
            if O_winner_check(board) is not None:
                win_index = O_winner_check(board) - 1
                board[win_index] = "O"
                print(f"I picked {win_index}")
                turn += 1
            else:
                block_index = winner_check(board) - 1
                board[block_index] = "O"
                print(f"I picked {block_index}")
                turn += 1
        elif turn > 4:
            if O_winner_check(board) is not None:
                win_index = O_winner_check(board) - 1
                board[win_index] = "O"
                print(f"I picked {win_index}")
                turn += 1
            else:
                block_index = winner_check(board) - 1
                board[block_index] = "O"
                print(f"I picked {block_index}")
                turn += 1



#computer_move(board, computer, human)
#print(board)
#           update the board with the move
#     display the board
#     switch turns
# congratulate the winner or declare a tie
def ttt_game():
    new_board()
    display_instructions()
    pieces()
    while end == 0:
        computer_move(board, computer,human)
        if turn == 1 and computer == "O":
            pass
        else:
            display_board(board)
        winner(board)
        if end == 0:
            human_move(board, human)
            display_board(board)
            winner(board)
    if mistake1 == 1:
        print("hint: As 2nd Player you must always go middle or you've signed up for a loss")
    if mistake2 == 1:
        print("hint: You cannot pick a corner after choosing the middle. You must pick a side 2 4 6 8 or you're a goner")
    print("Winner declared...")

exit = 0
while exit == 0:
    new_board()
    ttt_game()
    exit_var = ask_yes_no("Another game? y/n: ")
    if exit_var.lower() != "y":
        exit = 1
    else:
        end = 0
