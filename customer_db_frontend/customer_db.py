# To Do:
# -Search Functionality
# -Add Customer Functionality
# -Random 'None' printed when getting individual customer info?
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

def print_all_customers():
  print('\n--- Customers ---')
  rows = cursor.execute("SELECT customer_id, name, city, state, phone, email FROM Customers").fetchall();

  # columns = ['id', 'Name', 'City', 'State', 'Phone', 'Email']
  print(f'{"id":<2} {"Name":<25} {"City":<20} {"State":<10} {"Phone":<15} {"Email":<25}')

  for row in rows:
    try:
      print(f'{row[0]:<2} {row[1]:<25} {row[2]:<20} {row[3]:<10} {row[4]:<15} {row[5]:<25}')
    except:
      pass

def update_customer_info(field_to_update, new_value, customer_id):
  sql_update = f"UPDATE Customers SET {field_to_update}=? WHERE customer_id=?"
  update_values = (new_value, customer_id)
  cursor.execute(sql_update, update_values)
  connection.commit()

def delete_customer(id, name):
  really_delete = input(f'Are you SURE you want to DELETE Customer {id}:"{name}" (Y/N)? ')
  if really_delete.lower() == 'y':
    sql_delete = "DELETE FROM Customers WHERE customer_id=?"
    cursor.execute(sql_delete, (id,)).fetchone()
    connection.commit()
    print(f'SUCCESS: Customer "{name}" successfully Deleted!')


def view_customers():
  print_all_customers()
  customer_choice = input("\nEnter a Customer ID to View a Customer\nPress 'Enter' to return to Main Menu\n>>>")
  customer_info = get_customer_info(customer_choice)
  if customer_info:
    print(print_customer_details(customer_info))
    customer_id, customer_name, customer_address, customer_city, customer_state, customer_zipcode, customer_phone, customer_email = customer_info
    edit_customer_choice = input("\nTo update a field, enter the first letter of the field. \nTo delete this record, type 'DELETE'\nTo return to the main menu, press 'Enter'.\n>>>")
    if edit_customer_choice.lower() == 'i':
      print('\nThe ID cannot be changed.')
    elif edit_customer_choice.lower() == 'n':
      print(f'\nCurrent Name: {customer_name}')
      new_name = input('New Name: ')
      update_customer_info('name', new_name, customer_choice)
      print('SUCCESS: Name updated!')
    elif edit_customer_choice.lower() == 'a':
      print(f'\nCurrent Address: {customer_address}')
      new_address = input('New Address:')
      update_customer_info('street_address', new_address, customer_choice)
      print('SUCCESS: Address updated!')
    elif edit_customer_choice.lower() == 'c':
      print(f'\nCurrent City: {customer_city}')
      new_city = input('New City:')
      update_customer_info('city', new_city, customer_choice)
      print('SUCCESS: City updated!')
    elif edit_customer_choice.lower() == 's':
      print(f'\nCurrent State: {customer_state}')
      new_state = input('New State:')
      update_customer_info('state', new_state, customer_choice)
      print('SUCCESS: State updated!')
    elif edit_customer_choice.lower() == 'z':
      print(f'\nCurrent Zipcode: {customer_zipcode}')
      new_zipcode = input('New Zipcode:')
      update_customer_info('postal_code', new_zipcode, customer_choice)
      print('SUCCESS: Zipcode updated!')
    elif edit_customer_choice.lower() == 'p':
      print(f'\nCurrent Phone Number: {customer_phone}')
      new_phone_number = input('New Phone Number:')
      update_customer_info('phone', new_phone_number, customer_choice)
      print('SUCCESS: Phone Number updated!')
    elif edit_customer_choice.lower() == 'e':
      print(f'\nCurrent Email: {customer_email}')
      new_email = input('New Email:')
      update_customer_info('email', new_email, customer_choice)
      print('SUCCESS: Email updated!')
    elif edit_customer_choice.lower() == 'delete':
      delete_customer(customer_id, customer_name)
    elif edit_customer_choice == '':
      pass
    else:
      print('Invalid selection. Please try again.')

def search_customers():
  pass

def add_customer():
  pass


while True:
  choice = input('\n**** Customer Database ****\n\n[1] View All Customers\n[2] Search Customers\n[3] Add a New Customer\n[Q] Quit\n\n>>>')
  if choice == '1':
    view_customers()
  elif choice == '2':
    search_customers()
  elif choice == '3':
    add_customer
  elif choice.lower() == 'q':
    break
  else:
    print('\nPlease enter a valid choice from 1-3, or enter Q to quit.')