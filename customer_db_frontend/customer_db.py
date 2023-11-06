# To Do:
# -Add Customer Functionality
# -Make sure correct responses when incorrect options typed

import sqlite3
connection = sqlite3.connect('dp_customers.db')
cursor = connection.cursor()

def get_customer_info(id):
  try:
    customer_info = cursor.execute("SELECT customer_id, name, street_address, city, state, postal_code, phone, email FROM Customers WHERE customer_id=?", (id,)).fetchone()
    return customer_info
  except:
    return None

def print_customer_details(customer_info):
  # try:
  if customer_info:
    print('\n+++ Customer Detail +++\n')
    print(f"{'ID:':>9} {customer_info[0]}")
    print(f"{'Name:':>9} {customer_info[1]}")
    print(f"{'Address:':>9} {customer_info[2]}")
    print(f"{'City:':>9} {customer_info[3]}")
    print(f"{'State:':>9} {customer_info[4]}")
    print(f"{'Zipcode:':>9} {customer_info[5]}")
    print(f"{'Phone:':>9} {customer_info[6]}")
    print(f"{'Email:':>9} {customer_info[7]}")
  else:
    print('\n--- Invalid customer ID. Please try again ---')
  # except:
  #   return False

def get_all_customers():
  rows = cursor.execute("SELECT customer_id, name, city, state, phone, email FROM Customers").fetchall()
  return rows

def get_searched_customers(search_str):
  like_search_str = '%' + search_str + '%'
  sql_search = "SELECT customer_id, name, city, state, phone, email FROM Customers WHERE name LIKE ?"
  rows = cursor.execute(sql_search, (like_search_str,)).fetchall()
  return rows

def print_all_customers():
  print('\n--- Customers ---')
  rows = get_all_customers()
  print(f'{"id":<2} {"Name":<25} {"City":<20} {"State":<10} {"Phone":<15} {"Email":<25}')
  for row in rows:
    row_data = []
    for i in range(len(row)):
      if row[i]:
        row_data.append(row[i])
      else:
        row_data.append('None')
    try:
      print(f'{row_data[0]:<2} {row_data[1]:<25} {row_data[2]:<20} {row_data[3]:<10} {row_data[4]:<15} {row_data[5]:<25}')
    except:
      print('invalid row')

def update_choice(customer_info, customer_choice):
  if customer_info:
    print_customer_details(customer_info)
    customer_id, customer_name, customer_address, customer_city, customer_state, customer_zipcode, customer_phone, customer_email = customer_info
    edit_customer_choice = input("\nTo update a field, enter the first letter of the field. \nTo delete this record, type 'DELETE'\nTo return to the main menu, press 'Enter'.\n>>>")
    if edit_customer_choice.lower() == 'i':
      print('\nThe ID cannot be changed.')
    elif edit_customer_choice.lower() == 'n':
      print(f'\nCurrent Name: {customer_name}')
      new_name = input('New Name: ')
      update_customer_info('name', new_name, customer_choice, 'Name')
    elif edit_customer_choice.lower() == 'a':
      print(f'\nCurrent Address: {customer_address}')
      new_address = input('New Address: ')
      update_customer_info('street_address', new_address, customer_choice, 'Address')
    elif edit_customer_choice.lower() == 'c':
      print(f'\nCurrent City: {customer_city}')
      new_city = input('New City: ')
      update_customer_info('city', new_city, customer_choice, 'City')
    elif edit_customer_choice.lower() == 's':
      print(f'\nCurrent State: {customer_state}')
      new_state = input('New State: ')
      update_customer_info('state', new_state, customer_choice, 'State')
    elif edit_customer_choice.lower() == 'z':
      print(f'\nCurrent Zipcode: {customer_zipcode}')
      new_zipcode = input('New Zipcode: ')
      update_customer_info('postal_code', new_zipcode, customer_choice, 'Zipcode')
    elif edit_customer_choice.lower() == 'p':
      print(f'\nCurrent Phone Number: {customer_phone}')
      new_phone_number = input('New Phone Number: ')
      update_customer_info('phone', new_phone_number, customer_choice, 'Phone Number')
    elif edit_customer_choice.lower() == 'e':
      print(f'\nCurrent Email: {customer_email}')
      new_email = input('New Email: ')
      update_customer_info('email', new_email, customer_choice, 'Email')
    elif edit_customer_choice.lower() == 'delete':
      delete_customer(customer_id, customer_name)
      return False
    elif edit_customer_choice == '':
      return False
    else:
      print('Invalid selection. Please try again.')
    return True

def update_customer_info(field_to_update, new_value, customer_id, field_name):
  try:
    sql_update = f"UPDATE Customers SET {field_to_update}=? WHERE customer_id=?"
    update_values = (new_value, customer_id)
    cursor.execute(sql_update, update_values)
    connection.commit()
    print(f'SUCCESS: {field_name} updated!')
  except:
    print('- ERROR: Something went wrong. Make sure you did not use the same information as another customer for unique fields. -')

def delete_customer(id, name):
  really_delete = input(f'Are you SURE you want to DELETE Customer {id}:"{name}" (Y/N)? ')
  if really_delete.lower() == 'y':
    sql_delete = "DELETE FROM Customers WHERE customer_id=?"
    cursor.execute(sql_delete, (id,)).fetchone()
    connection.commit()
    print(f'SUCCESS: Customer "{name}" successfully Deleted!')


def view_customers_option():
  print_all_customers()
  select_customer()
  # customer_choice = input("\nEnter a Customer ID to View a Customer\nPress 'Enter' to return to Main Menu\n>>>")
  # while True:
  #   customer_info = get_customer_info(customer_choice,)
  #   continue_loop = update_choice(customer_info, customer_choice)
  #   if not continue_loop:
  #     break

def search_customers_option():
  search_str = input('\nSearch Term: ')
  rows = get_searched_customers(search_str)
  print(f'{"id":<2} {"Name":<25} {"City":<20} {"State":<10} {"Phone":<15} {"Email":<25}')
  for row in rows:
    row_data = []
    for i in range(len(row)):
      if row[i]:
        row_data.append(row[i])
      else:
        row_data.append('None')
    try:
      print(f'{row_data[0]:<2} {row_data[1]:<25} {row_data[2]:<20} {row_data[3]:<10} {row_data[4]:<15} {row_data[5]:<25}')
    except:
      print('invalid row')
  select_customer()
  # customer_choice = input("\nEnter a Customer ID to View a Customer\nPress 'Enter' to return to Main Menu\n>>>")
  # while True:
  #   customer_info = get_customer_info(customer_choice,)
  #   continue_loop = update_choice(customer_info, customer_choice)
  #   if not continue_loop:
  #     break

def select_customer():
  customer_choice = input("\nEnter a Customer ID to View a Customer\nPress 'Enter' to return to Main Menu\n>>>")
  while True:
    customer_info = get_customer_info(customer_choice,)
    continue_loop = update_choice(customer_info, customer_choice)
    if not continue_loop:
      break

def add_customer_option():
  pass

while True:
  choice = input('\n**** Customer Database ****\n\n[1] View All Customers\n[2] Search Customers\n[3] Add a New Customer\n[Q] Quit\n\n>>>')
  if choice == '1':
    view_customers_option()
  elif choice == '2':
    search_customers_option()
  elif choice == '3':
    add_customer_option()
  elif choice.lower() == 'q':
    break
  else:
    print('\nPlease enter a valid choice from 1-3, or enter Q to quit.')