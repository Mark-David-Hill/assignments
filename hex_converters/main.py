def hex_to_dec(hex_str):
  dec_values = []
  dec_value = 0
  current_multipier = 1
  for character in hex_str:
    current_value = 0
    if character.lower() == 'a':
      current_value = 10
    elif character.lower() == 'b':
      current_value = 11
    elif character.lower() == 'c':
      current_value = 12
    elif character.lower() == 'd':
      current_value = 13
    elif character.lower() == 'e':
      current_value = 14
    elif character.lower() == 'f':
      current_value = 15
    else:
      current_value = int(character)
    
    dec_values.insert(0, current_value)

  for current_value in dec_values:
    value_to_add = current_value * current_multipier
    dec_value += value_to_add
    current_multipier *= 16

  return dec_value
    
def dec_to_hex(dec_num):
  remainders = []
  current_value = int(dec_num)
  while current_value >= 1:
    quotient = current_value // 16
    remainder = current_value % 16
    remainders.insert(0, remainder)
    current_value = quotient
  
  hex_str = ''
  for remainder in remainders:
    if remainder == 10:
      hex_str += 'A'
    elif remainder == 11:
      hex_str += 'B'
    elif remainder == 12:
      hex_str += 'C'
    elif remainder == 13:
      hex_str += 'D'
    elif remainder == 14:
      hex_str += 'E'
    elif remainder == 15:
      hex_str += 'F'
    else:
      hex_str += str(remainder)

  return hex_str

has_quit = False
print('*** Hexadecimal Converter ***')

while has_quit is False:
  dash = '-'
  print(dash * 20)
  print('(H)exadecimal to Decimal Conversion\n(D)ecimal to Hexadecimal Conversion\n(Q)uit')
  choice = input()
  try:
    if choice.lower() == 'h':
      chosen_hex = input('Enter a Hexadecimal Number: ')
      print('= ' + str(hex_to_dec(chosen_hex)))
    elif choice.lower() == 'd':
      chosen_number = input('Enter a Decimal Number: ')
      print('= ' + dec_to_hex(chosen_number))
    elif choice.lower() == 'q':
      print('\nGoodbye!')
      has_quit = True
      break
    else:
      print("I didn't understand your selection. Please type the letter corresponding with your choice and press enter.")
  except:
    print("Something went wrong. Please check your input and try again.")
  
  input('\nPress <enter> to continue')