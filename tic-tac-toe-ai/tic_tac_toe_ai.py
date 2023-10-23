import random

winning_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

corner_ids = [0, 2, 6, 8]
edge_ids = [1, 3, 5, 7]
center_id = 4

def get_available_moves(board):
   output = []
   for i in range(len(board)):
      if board[i] == '':
         output.append(i)
   
   return output

def get_winning_moves(board, letter):
   moves = []
   for set in winning_combinations:
    letter_controlled_spaces = 0
    open_space = None
    for win_space in range(3):
      possible_win_space_id = set[win_space]
      if board[possible_win_space_id] == letter:
         letter_controlled_spaces += 1
      elif board[possible_win_space_id] == '':
         open_space = possible_win_space_id
      
      if open_space != None and letter_controlled_spaces == 2:
         moves.append(open_space)
   
   if len(moves) > 0:
      return moves
   else:
      return None

def get_move(board, letter):
   opponent_letter = ''
   if letter == 'X':
     opponent_letter = 'O'
   else:
     opponent_letter = 'X'
   # If win move is available for you, take it. If not but is available for opponent, block them
   available_moves = get_available_moves(board)
   winning_moves = get_winning_moves(board, letter)
   opponent_winning_moves = get_winning_moves(board, opponent_letter)
   if winning_moves != None:
     return random.choice(winning_moves)
   elif opponent_winning_moves != None:
     return random.choice(opponent_winning_moves)
   # If all spaces are available or it's the second turn and the center is taken, take a corner
   elif len(available_moves) == 9 or (len(available_moves) == 8 and not center_is_available(available_moves)):
      return random.choice([0, 2, 6, 8])
   # On second turn if not taken, take center
   elif len(available_moves) == 8 and center_is_available(available_moves):
   # and at_least_one_corner_is_occupied(board):
      return center_id
   # Turn 3- take an adjacent corner not adjacent to an opponent's letter
   elif len(available_moves) == 7:
   # and center_is_available(available_moves):
      my_corner_id = get_letter_spaces(board, letter)[0]
      opponent_controlled_space = get_letter_spaces(board, opponent_letter)[0]
      adjacent_corners = get_adjacent_corners(my_corner_id)
      for corner in adjacent_corners:
         if corner != opponent_controlled_space:
            corner_is_ok = True
            adjacent_spaces = get_adjacent_spaces(corner)
            for space in adjacent_spaces:
               if space == opponent_controlled_space:
                  corner_is_ok = False
            
            if corner_is_ok:
               return corner
            
   # If setting up trap on turn 5, place in corner with no adjacent 'O's.
   elif len(available_moves) == 5 and center_is_available(available_moves):
      for move in available_moves:
         opponent_controlled_spaces = get_letter_spaces(board, opponent_letter)
         if move != 4 and move % 2 == 0:
            corner_is_ok = True
            adjacent_spaces = get_adjacent_spaces(move)
            for space in adjacent_spaces:
               if space in opponent_controlled_spaces:
                  corner_is_ok = False
            if corner_is_ok:
               return move
   # On turn 4, if X's in opposite corners and O in middle, place on an edge, not another corner.
   elif len(available_moves) == 6 and (board[0] == 'X' and board[8] == 'X') or (board[2] == 'X' and board[6] == 'X'):
      return random.choice(edge_ids)


   # Check for potential traps. If any, block them.
   else:
      # return random.choice(available_moves)
      possible_trap_moves = []
      for move in available_moves:
         test_board = []
         for space in board:
            test_board.append(space)
         test_board[move] = opponent_letter
         test_opponent_win_moves = get_winning_moves(test_board, opponent_letter)
         if test_opponent_win_moves and len(test_opponent_win_moves) >= 2:
            possible_trap_moves.append(move)
          
      if len(possible_trap_moves) > 0:
         return possible_trap_moves[0]
      else:
         # return 7
         return random.choice(available_moves)

def at_least_one_corner_is_occupied(board):
   corners = [board[0], board[2], board[6], board[8]]
   for corner in corners:
      if corner != '':
         return True
   
   return False

def get_adjacent_corners(corner_id):
   if corner_id == 0 or corner_id == 8:
      return [2, 6]
   elif corner_id == 2 or corner_id == 6:
      return [0, 8]
   
def get_opposite_corner(corner_id):
   if corner_id == 0:
      return 8
   elif corner_id == 2:
      return 6
   elif corner_id == 6:
      return 2
   elif corner_id == 8:
      return 0
   
def center_is_available(available_moves):
   if center_id in available_moves:
      return True
   else:
      return False

def get_letter_spaces(board, letter):
   my_letter_spaces = []
   for i in range(len(board)):
      if board[i] == letter:
         my_letter_spaces.append(i)
   
   return my_letter_spaces

def get_adjacent_spaces(space_id):
   if space_id == 0:
      return [1, 3]
   elif space_id == 1:
      return [0, 2, 4]
   elif space_id == 2:
      return [1, 5]
   elif space_id == 3:
      return [0, 4, 6]
   elif space_id == 4:
      return [1, 3, 5, 7]
   elif space_id == 5:
      return [2, 4, 8]
   elif space_id == 6:
      return [3, 7]
   elif space_id == 7:
      return [4, 6, 8]
   elif space_id == 8:
      return [5, 7]

   
# my_board = ['', '', 'X', 'O', 'X', 'O', 'O', '', 'X']
# my_letter = 'X'

# # for i in range(30):
# print(get_move(my_board, my_letter))