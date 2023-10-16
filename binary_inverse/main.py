def bin_add_one(bin_str_1):
  error_message = 'Please enter a valid binary number'
  bin_one = '00000001'
  try:
      sum_str = ''
      current_index = 7
      sum_list = ['', '','','','','','','']
      carry = 0

      while current_index >= 0:
        if bin_str_1[current_index] == '0' and bin_one[current_index] == '0':
          if carry == 1:
            sum_list[current_index] = '1'
            carry = 0
          elif carry == 0:
            sum_list[current_index] = '0'
        elif (bin_str_1[current_index] == '1' and bin_one[current_index] == '0') or (bin_str_1[current_index] == '0' and bin_one[current_index] == '1'):
          if carry == 1:
            sum_list[current_index] = '0'
            carry = 1
          elif carry == 0:
            sum_list[current_index] = '1'
        elif (bin_str_1[current_index] == '1' and bin_one[current_index] == '1'):
          if carry == 1:
            sum_list[current_index] = '1'
            carry = 1
          elif carry == 0:
            sum_list[current_index] = '0'
            carry = 1

        current_index = current_index - 1

      for byte_str in sum_list:
        sum_str += byte_str

      return sum_str
  except:
    return error_message
  
def invert_1_and_0(bin_str):
  new_str = ''
  for i in range(len(bin_str)):
    if bin_str[i] == '0':
      new_str += '1'
    elif bin_str[i] == '1':
      new_str += '0'
  return new_str

def bin_inverse(bin_str):
  inverted_str = invert_1_and_0(bin_str)
  twos_complement = bin_add_one(inverted_str)
  return twos_complement

has_quit = False
print('*** Binary Inverse Calculator ***')

while has_quit is False:
  dash = '-'
  print(dash * 20)
  choice = input("Please input a binary number to get the two's complement inverse:")
  try:
    if choice.lower() == 'q':
      print('\nGoodbye!')
      has_quit = True
      break
    else:
      print(bin_inverse(choice))
  except:
    print("Please input a valid binary number")
  
  input('\nPress <enter> to continue')