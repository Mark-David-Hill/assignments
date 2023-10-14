# Note to grader- The random module was imported just for testing and isn't used in the actual binary calculations. All test code is commented out but available if you want to take a look at it.
# import random

def bin_str_from_list(str_list):
  new_bin_str = ''
  for str in str_list:
    new_bin_str += str
  return new_bin_str

def dec_to_bin(dec_num):
  error_message = 'Please enter a valid integer.'
  try:
    int_to_convert = int(dec_num)
    if int_to_convert >= 0 and int_to_convert <= 255:
      binary_number = ''
      decimal_place = 0
      while decimal_place < 8:
        multiples_of_2 = [128, 64, 32, 16, 8, 4, 2, 1]
        multiple_of_2_index = decimal_place
        current_multiple_of_2 = multiples_of_2[multiple_of_2_index]
        decimal_place += 1

        if int_to_convert >= current_multiple_of_2:
          binary_number += '1'
          int_to_convert = int_to_convert - current_multiple_of_2
        else:
          binary_number += '0'

      return binary_number
    else:
      return error_message
  except:
    return error_message

def bin_to_dec(bin_str):
  error_message = 'Please enter a valid binary number.'
  try:
      current_int = 0
      decimal_place = 0
      multiples_of_2 = [128, 64, 32, 16, 8, 4, 2, 1]
      while decimal_place < 8:
        multiple_of_2_index = decimal_place
        current_multiple_of_2 = multiples_of_2[multiple_of_2_index]
        
        if int(bin_str[decimal_place]) == 0:
          pass
        elif int(bin_str[decimal_place]) == 1:
          current_int += current_multiple_of_2
        decimal_place += 1

      return current_int
  except:
    return error_message

def bin_addition(bin_str_1, bin_str_2):
  error_message = 'Please enter 2 valid binary numbers.'
  try:
      sum_str = ''
      current_index = 7
      sum_list = ['', '','','','','','','']
      carry = 0

      while current_index >= 0:
        if bin_str_1[current_index] == '0' and bin_str_2[current_index] == '0':
          if carry == 1:
            sum_list[current_index] = '1'
            carry = 0
          elif carry == 0:
            sum_list[current_index] = '0'
        elif (bin_str_1[current_index] == '1' and bin_str_2[current_index] == '0') or (bin_str_1[current_index] == '0' and bin_str_2[current_index] == '1'):
          if carry == 1:
            sum_list[current_index] = '0'
            carry = 1
          elif carry == 0:
            sum_list[current_index] = '1'
        elif (bin_str_1[current_index] == '1' and bin_str_2[current_index] == '1'):
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

def bin_subtraction(bin_str_1, bin_str_2):
  error_message = 'Please enter 2 valid binary numbers.'
  try:
    dec1 = bin_to_dec(bin_str_1)
    dec2 = bin_to_dec(bin_str_2)
    if dec1 < dec2:
      return 'Error: Negative result'

    difference_str = ''
    current_index = 7
    difference_list = ['','','','','','','','']
    borrow = 0

    while current_index >= 0:
      if bin_str_1[current_index] == '0' and bin_str_2[current_index] == '0':
        if borrow == 1:
          difference_list[current_index] = '1'
        elif borrow == 0:
          difference_list[current_index] = '0'
        elif borrow == 2:
          difference_list[current_index] = '1'
      elif (bin_str_1[current_index] == '1' and bin_str_2[current_index] == '0'):
        if borrow == 1:
          difference_list[current_index] = '0'
          borrow = 0
        elif borrow == 0:
          difference_list[current_index] = '1'
      elif (bin_str_1[current_index] == '0' and bin_str_2[current_index] == '1'):
        if borrow == 1:
          difference_list[current_index] = '0'
          borrow == 2
        elif borrow == 0:
          difference_list[current_index] = '1'
          borrow = 1
        elif borrow == 2:
          difference_list[current_index] = '0'
      elif (bin_str_1[current_index] == '1' and bin_str_2[current_index] == '1'):
        if borrow == 1:
          difference_list[current_index] = '1'
          borrow = 1
        elif borrow == 0:
          difference_list[current_index] = '0'

      current_index = current_index - 1

    for byte_str in difference_list:
      difference_str += byte_str

    return difference_str
  except:
    return error_message

def bin_multiplication(bin_str_1, bin_str_2):
  error_message = 'Please enter 2 valid binary numbers.'
  try:
      product_str = ''
      step_lists = [
        ['','','','','','','',''],
        ['','','','','','','','0'],
        ['','','','','','','0','0'],
        ['','','','','','0','0','0'],
        ['','','','','0','0','0','0'],
        ['','','','0','0','0','0','0'],
        ['','','0','0','0','0','0','0'],
        ['','0','0','0','0','0','0','0']
      ]

      step_index = 0
      starting_binary_index = 7

      while step_index <= 7:
        binary_index = starting_binary_index
        bin_2_index = 7
        base_multiplier = int(bin_str_1[binary_index])
        while binary_index >= 0:
          if base_multiplier == 0:
            step_lists[step_index][binary_index] = '0'
          elif base_multiplier == 1:
            if bin_str_2[bin_2_index] == '0':
              step_lists[step_index][binary_index] = '0'
            elif bin_str_2[bin_2_index] == '1':
              step_lists[step_index][binary_index] = '1'
          binary_index -= 1
          bin_2_index -= 1
        step_index += 1
        starting_binary_index -= 1

      current_index = 0
      while current_index <= 7:
        if current_index == 0:
          product_str = bin_str_from_list(step_lists[current_index])
        else:
          product_str = bin_addition(product_str, bin_str_from_list(step_lists[current_index]))
        current_index += 1

      return product_str
  except:
    return error_message

def bin_division(bin_str_1, bin_str_2):
  error_message = 'Please enter 2 valid binary numbers.'
  try:
    quotient_str = ''
    remainder_str = ''
    extra_remainder_zeroes = 0

    leading_zeros_by_step_index = [7, 6, 5, 4, 3, 2, 1, 0]
    current_step_append_to_start_bin = bin_str_1

    for i in range(8):
      current_step_bin = ''
      append_index = 0
      for j in range(8):
        if j < (leading_zeros_by_step_index[i]):
          current_step_bin += '0'
        else:
          current_step_bin += current_step_append_to_start_bin[append_index]
          append_index += 1

      dec_to_compare_1 = bin_to_dec(current_step_bin)
      dec_to_compare_2 = bin_to_dec(bin_str_2)    

      if dec_to_compare_1 >= dec_to_compare_2:
        quotient_str += '1'
        bin_to_subtract_from = current_step_append_to_start_bin
        shifted_string = ''
        amount_to_shift = 7 - i

        for j in range(8):
          if j > 7 - amount_to_shift:
            shifted_string += '0'
          else:
            shifted_string += bin_str_2[j + amount_to_shift]
        bin_to_subract = shifted_string
        extra_remainder_zeroes = 0
        current_step_append_to_start_bin = bin_subtraction(bin_to_subtract_from, bin_to_subract)
      else:
        quotient_str += '0'
        extra_remainder_zeroes += 1

      remainder_str = current_step_append_to_start_bin

    return f'{quotient_str} Remainder: {remainder_str}'
  except:
    return error_message

# Testing Code
####################################################################################################################

# def create_random_bin():
#   bin_str = ''
#   for _ in range(8):
#     rand_num = int(bool(random.getrandbits(1)))
#     rand_num_str = str(rand_num)
#     bin_str += rand_num_str
#   return bin_str

# def get_expected_bin_sum(bin1, bin2):
#   dec1 = bin_to_dec(bin1)
#   dec2 = bin_to_dec(bin2)
#   dec_sum = dec1 + dec2

#   bin_sum = dec_to_bin(dec_sum)
#   return bin_sum

# def get_expected_bin_difference(bin1, bin2):
#   dec1 = bin_to_dec(bin1)
#   dec2 = bin_to_dec(bin2)
#   dec_difference = dec1 - dec2

#   bin_difference = dec_to_bin(dec_difference)
#   return bin_difference

# def get_expected_bin_product(bin1, bin2):
#   dec1 = bin_to_dec(bin1)
#   dec2 = bin_to_dec(bin2)
#   dec_product = dec1 * dec2

#   bin_product = dec_to_bin(dec_product)
#   return bin_product

# def get_expected_bin_quotient(bin1, bin2):
#   dec1 = bin_to_dec(bin1)
#   dec2 = bin_to_dec(bin2)
#   dec_quotient = dec1 / dec2
#   remainder = dec1 % dec2

#   bin_quotient = dec_to_bin(dec_quotient)
#   bin_remainder = dec_to_bin(remainder)
#   remainder_str = str(bin_remainder)
#   return f'{bin_quotient} Remainder: {remainder_str}'

# def test_bin_addition(bin1, bin2):
#   expected_sum = get_expected_bin_sum(bin1, bin2)
#   if expected_sum == 'Please enter a valid integer.':
#     print('Answer exceeded range (above 255)\n')
#   else:
#     print(f'numbers: {bin1}, {bin2}')
#     print('expected sum:')
#     print(expected_sum)
#     print('actual sum:')
#     actual_sum = bin_addition(bin1, bin2)
#     print(actual_sum)
#     if expected_sum == actual_sum:
#       print('Addition was successful! :)\n')
#     else:
#       print('*** Addition failed :( ***\n')

# def test_bin_subtraction(bin1, bin2):

#   if bin1 >= bin2:
#     minuend = bin1
#     subtrahend = bin2
#   else:
#     minuend = bin2
#     subtrahend = bin1
#   expected_difference = get_expected_bin_difference(minuend, subtrahend)
#   print(f'numbers: {minuend}, {subtrahend}')
#   print('expected difference:')
#   print(expected_difference)
#   print('actual difference:')
#   actual_difference = bin_subtraction(minuend, subtrahend)
#   print(actual_difference)
#   if expected_difference == actual_difference:
#     print('Subtraction was successful! :) \n')
#   else:
#     print('*** Subtraction failed :( ***\n')

# def test_bin_multiplication(bin1, bin2):
#   expected_product = get_expected_bin_product(bin1, bin2)
#   if expected_product == 'Please enter a valid integer.':
#     print('Answer exceeded range (above 255)\n')
#   else:
#     print(f'numbers: {bin1}, {bin2}')
#     print('expected product:')
#     print(expected_product)
#     print('actual product:')
#     actual_product = bin_multiplication(bin1, bin2)
#     print(actual_product)
#     if expected_product == actual_product:
#       print('Multiplication was successful! :) \n')
#     else:
#       print('*** Multiplication failed :( ***\n')

# def test_bin_division(bin1, bin2):
#   if bin1 >= bin2:
#     dividend = bin1
#     divisor = bin2
#   else:
#     dividend = bin2
#     divisor = bin1
#   expected_quotient = get_expected_bin_quotient(dividend, divisor)
#   print(f'numbers: {dividend}, {divisor}')
#   print('expected quotient:')
#   print(expected_quotient)
#   print('actual quotient:')
#   actual_quotient = bin_division(dividend, divisor)
#   print(actual_quotient)
#   if expected_quotient == actual_quotient:
#     print('Division was successful! :) \n')
#   else:
#     print('*** Division failed :( ***\n')

# for _ in range(1000):
#   bin1 = create_random_bin()
#   bin2 = create_random_bin()
#   # Testing note: Uncomment whatever type of operation you want to test.
#   # test_bin_addition(bin1, bin2)
#   # test_bin_subtraction(bin1, bin2)
#   # test_bin_multiplication(bin1, bin2)
#   # test_bin_division(bin1, bin2)

####################################################################################################################

has_quit = False
print('*** Binary Calculator ***')

while has_quit is False:
  dash = '-'
  print(dash * 20)
  print('(B)inary to Decimal Conversion\n(D)ecimal to Binary Conversion\n(A)dd two Binary Numbers\n(S)ubtract two Binary Numbers\n(M)ultiply two Binary Numbers\nD(i)vide two Binary Numbers\n(Q)uit')
  choice = input()
  try:
    if choice.lower() == 'b':
      chosen_bin = input('Enter a Binary Number (8-digits): ')
      print('= ' + str(bin_to_dec(chosen_bin)))
    elif choice.lower() == 'd':
      chosen_number = input('Enter a Decimal Number (0-255): ')
      print('= ' + dec_to_bin(chosen_number))
    elif choice.lower() == 'a':
      bin_str_1 = input('Enter the first binary number : ')
      bin_str_2 = input('Enter the second binary number: ')
      print('= ' + bin_addition(bin_str_1, bin_str_2))
    elif choice.lower() == 's':
      bin_str_1 = input('Enter the first binary number : ')
      bin_str_2 = input('Enter the second binary number: ')
      print('= ' + bin_subtraction(bin_str_1, bin_str_2))
    elif choice.lower() == 'm':
      bin_str_1 = input('Enter the first binary number : ')
      bin_str_2 = input('Enter the second binary number: ')
      print('= ' + bin_multiplication(bin_str_1, bin_str_2))
    elif choice.lower() == 'i':
      bin_str_1 = input('Enter the first binary number : ')
      bin_str_2 = input('Enter the second binary number: ')
      print('= ' + bin_division(bin_str_1, bin_str_2))
    elif choice.lower() == 'q':
      print('\nGoodbye!')
      has_quit = True
      break
  except:
    print("I didn't understand your selection. Please type the letter corresponding with your choice and press enter.")
  
  input('\nPress <enter> to continue')