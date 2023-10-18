def get_winner(board):
  winning_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

  for set in winning_combinations:
    if board[set[0]] == 'X' and board[set[1]] == 'X' and board[set[2]] == 'X':
      return 'X'
    elif board[set[0]] == 'O' and board[set[1]] == 'O' and board[set[2]] == 'O':
      return 'O'
  
  return ''


board = ['X', '', 'X', 'O', 'O', '', '', 'X', 'O']
print(get_winner(board) == '')

board = ['X', '', 'X', 'O', 'O', 'O', 'X', 'X', 'O']
print(get_winner(board) == 'O')

board = ['X', '', 'X', 'X', 'O', 'O', 'X', '', 'O']
print(get_winner(board) == 'X')

board = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'X', 'O']
print(get_winner(board) == 'X')

board = ['', '', '', '', 'O', '', 'X', '', '']
print(get_winner(board) == '')