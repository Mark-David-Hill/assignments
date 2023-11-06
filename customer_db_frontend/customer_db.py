import sqlite3
connection = sqlite3.connect('dp_customers.db')
cursor = connection.cursor()

def print_customer_details(id):
  # try:
  customer_info = cursor.execute("SELECT customer_id, name, street_address, city, state, postal_code, phone, email FROM Customers WHERE customer_id=?", (id,)).fetchone()
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
    return True
  else:
    print('\n--- Invalid customer ID. Please try again ---')
  # except:
  #   return False

def print_all_customers():
  print('\n--- Customers ---')
  rows = cursor.execute("SELECT customer_id, name, city, state, phone, email FROM Customers").fetchall();

  columns = ['id', 'Name', 'City', 'State', 'Phone', 'Email']
  print(f'{"id":<2} {"Name":<25} {"City":<25} {"State":<25} {"Phone":<25} {"Email":<25}')

  for row in rows:
    try:
      print(f'{row[0]:<2} {row[1]:<25} {row[2]:<25} {row[3]:<25} {row[4]:<25} {row[5]:<25}')
    except:
      pass

def update_customer_info(field_to_update, new_value, customer_id):
  sql_update = f"UPDATE Customers SET {field_to_update}=? WHERE customer_id=?"
  update_values = (new_value, customer_id)
  cursor.execute(sql_update, update_values)
  connection.commit()

def view_customers():
  print_all_customers()
  customer_choice = input("\nEnter a Customer ID to View a Customer\nPress 'Enter' to return to Main Menu\n>>>")
  is_valid_customer = print_customer_details(customer_choice)
  if is_valid_customer:
    edit_customer_choice = input("\nTo update a field, enter the first letter of the field. \nTo delete this record, type 'DELETE'\nTo return to the main menu, press 'Enter'.\n>>>")
    if edit_customer_choice.lower() == 'i':
      print('\nThe ID cannot be changed.')
    elif edit_customer_choice.lower() == 'n':
      print('\nCurrent Name:')
      new_name = input('New Name:')
      update_customer_info('name', new_name, customer_choice)
    elif edit_customer_choice.lower() == 'a':
      print('\nCurrent Address:')
      new_address = input('New Address:')
      update_customer_info('stret_address', new_address, customer_choice)
    elif edit_customer_choice.lower() == 'c':
      print('\nCurrent City:')
      new_city = input('New City:')
      update_customer_info('city', new_city, customer_choice)
    elif edit_customer_choice.lower() == 's':
      print('\nCurrent State:')
      new_state = input('New State:')
      update_customer_info('state', new_state, customer_choice)
    elif edit_customer_choice.lower() == 'z':
      print('\nCurrent Zipcode:')
      new_zipcode = input('New Zipcode:')
      update_customer_info('postal_code', new_zipcode, customer_choice)
    elif edit_customer_choice.lower() == 'p':
      print('\nCurrent Phone Number:')
      new_phone_number = input('New Phone Number:')
      update_customer_info('phone', new_phone_number, customer_choice)
    elif edit_customer_choice.lower() == 'e':
      print('\nCurrent Email:')
      new_email = input('New Email:')
      update_customer_info('email', new_email, customer_choice)
    elif edit_customer_choice.lower() == 'delete':
      pass
      
    else:
      print('Invalid selection. Please try again.')

def search_customers():
  pass

def add_customer():
  pass



while True:
  choice = input('\n**** Customer Database ****\n\n[1] View All Customers\n[2] Search Customers\n[3]Add a New Customer\n[Q]Quit\n\n>>>')
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