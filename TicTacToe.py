def display_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the left
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        # small bug here where if str is supplied program breaks
    return position

def replay():
    return input('Do you want to play again? Enter Yes or No: ')

print('Welcome to Tic Tac Toe!')


#Game itself
while True:
    # Reset the board
    the_board = [' '] * 10
    player1_marker = 'X'
    player2_marker = 'O'
    turn = 'Player 1'
    print("Player 1 is X and will go first.")
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_open = True
    elif play_game.lower()[0] == 'n':
        game_open = False
        print("Come back when you are ready!")
        break
    else:
        game_open = False
        print("I think you are drunk, come back when you are sober!")
        break

    while game_open:
        if turn == 'Player 1':
            print("Your turn Player 1.")
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player1_marker, position)

            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Player 1 has won!')
                game_open = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("It's a tie!")
                    break
                else:
                    turn = 'Player 2'

        else:
            print("Your turn Player 2.")
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)

            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 has won!')
                game_open = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("It's a tie!")
                    break
                else:
                    turn = 'Player 1'
    if replay() == 'No':
            break