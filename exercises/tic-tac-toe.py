def display_board(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
# boards = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
boards = [' '] * 10
# display_board(boards)

def user_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player 1: Do you want to be X or O? ').upper()
    player1 = marker
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    print(f'Player 1 is {player1} and Player 2 is {player2}')
user_input()