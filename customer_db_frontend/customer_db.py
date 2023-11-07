# Note to Grader:
# When this is run, it will check if an 'active' column exists in the Customers table. 
# If not, it will add an 'active' column and set it to True for all entries.
# To activate an inactive customer, select the corresponding option from the main menu
# To deactivate an active customer you can do so after viewing all active customers and selecting one to view details for.

import sqlite3
connection = sqlite3.connect('dp_customers.db')
cursor = connection.cursor()

def get_customer_info(id, active):
  try:
    customer_info = cursor.execute("SELECT customer_id, name, street_address, city, state, postal_code, phone, email FROM Customers WHERE customer_id=? AND active=?", (id, active)).fetchone()
    return customer_info
  except Exception as e:
    print(f'\n- ERROR: {e}. Could not retrieve customer information. -')
    return None

def print_customer_details(customer_info):
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

def get_all_active_customers():
  try:
    rows = cursor.execute("SELECT customer_id, name, city, state, phone, email FROM Customers WHERE active=True").fetchall()
    return rows
  except Exception as e:
    print(f'\n- ERROR: {e}. Customer data could not be loaded. -')

def get_all_inactive_customers():
  try:
    rows = cursor.execute("SELECT customer_id, name, city, state, phone, email FROM Customers WHERE active=False").fetchall()
    return rows
  except Exception as e:
    print(f'\n- ERROR: {e}. Customer data could not be loaded. -')

def get_searched_customers(search_str):
  like_search_str = '%' + search_str + '%'
  sql_search = "SELECT customer_id, name, city, state, phone, email FROM Customers WHERE active = True AND name LIKE ?"
  rows = cursor.execute(sql_search, (like_search_str,)).fetchall()
  return rows

def print_all_active_customers():
  print('\n--- Customers ---')
  rows = get_all_active_customers()
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
    except Exception as e:
      print(f'\n- ERROR: {e}. Could not print row data for customer -')

def print_all_inactive_customers():
  rows = get_all_inactive_customers()
  if rows:
    print('\n--- Inactive Customers ---')
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
      except Exception as e:
        print(f'\n- ERROR: {e}. Could not print row data for customer -')
    return True
  else:
    print(f'\n- There are currently no Inactive Customers -')
    return False

def update_choice(customer_info, customer_choice):
  if customer_info:
    print_customer_details(customer_info)
    customer_id, customer_name, customer_address, customer_city, customer_state, customer_zipcode, customer_phone, customer_email = customer_info
    edit_customer_choice = input("\nTo update a field, enter the first letter of the field. \nTo delete this record, type 'DELETE'\nTo deactivate this record, type 'DEACTIVATE'\nTo return to the main menu, press 'Enter'.\n>>>")
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
    elif edit_customer_choice.lower() == 'deactivate':
      deactivate_customer(customer_id, customer_name)
      return False
    elif edit_customer_choice == '':
      return False
    else:
      print('- Invalid selection. Please try again. -')
    return True

def update_customer_info(field_to_update, new_value, customer_id, field_name):
  try:
    sql_update = f"UPDATE Customers SET {field_to_update}=? WHERE customer_id=?"
    update_values = (new_value, customer_id)
    cursor.execute(sql_update, update_values)
    connection.commit()
    print(f'SUCCESS: {field_name} updated!')
  except Exception as e:
    print(f'\n- ERROR: {e}. Customer data was not updated. -')

def delete_customer(id, name):
  while True:
    really_delete = input(f'\nAre you SURE you want to DELETE Customer {id}:"{name}" (Y/N)? ')
    if really_delete.lower() == 'y':
      sql_delete = "DELETE FROM Customers WHERE customer_id=?"
      cursor.execute(sql_delete, (id,)).fetchone()
      connection.commit()
      print(f'SUCCESS: Customer "{name}" successfully Deleted!')
      break
    elif really_delete.lower() != 'n':
      print('\n- ERROR: Invalid Response. Please try again. -')
    else:
      break

def view_customers_option():
  print_all_active_customers()
  select_customer()

def search_customers_option():
  search_str = input('\nSearch Term: ')
  rows = get_searched_customers(search_str)
  if rows:
    print(f'\n{"id":<2} {"Name":<25} {"City":<20} {"State":<10} {"Phone":<15} {"Email":<25}')
    for row in rows:
      row_data = []
      for i in range(len(row)):
        if row[i]:
          row_data.append(row[i])
        else:
          row_data.append('None')
      try:
        print(f'{row_data[0]:<2} {row_data[1]:<25} {row_data[2]:<20} {row_data[3]:<10} {row_data[4]:<15} {row_data[5]:<25}')
      except Exception as e:
        print(f'\n- ERROR: {e}. Could not print row data for customer -')
    select_customer()
  else:
    print(f'\n- No search results found for "{search_str}" -')

def select_customer():
  customer_choice = input("\nEnter a Customer ID to View a Customer\nPress 'Enter' to return to Main Menu\n>>>")
  while True:
    customer_info = get_customer_info(customer_choice, True)
    if customer_info:
      continue_loop = update_choice(customer_info, customer_choice)
      if not continue_loop:
        break
    elif customer_choice == '':
      break
    else:
      print('\n- ERROR: Invalid Customer ID. Returning to the Main Menu. -')
      break

def add_customer_option():
  print('\nPlease fill out the form below to add a new Customer:\n')
  field_choices = []
  field_choices.append(input(f"{'Name:':>9} "))
  field_choices.append(input(f"{'Address:':>9} "))
  field_choices.append(input(f"{'City:':>9} "))
  field_choices.append(input(f"{'State:':>9} "))
  field_choices.append(input(f"{'Zipcode:':>9} "))
  field_choices.append(input(f"{'Phone:':>9} "))
  field_choices.append(input(f"{'Email:':>9} "))

  # name, address, city, state, zipcode, phone, email = field_choices
  insert_sql = "INSERT INTO Customers (name, street_address, city, state, postal_code, phone, email, active) VALUES (?, ?, ?, ?, ?, ?, ?, True)"
  try:
    cursor.execute(insert_sql, field_choices)
    connection.commit()
    print(f'\nSUCCESS: Customer "{field_choices[0]}" Successfully added!')
  except Exception as e:
    print(f'\n- ERROR: {e}. Customer was not added. -')

def activate_customer(customer_id):
  try:
    sql_update = f"UPDATE Customers SET active=True WHERE customer_id=?"
    update_values = (customer_id,)
    cursor.execute(sql_update, update_values)
    connection.commit()
    print(f'\nSUCCESS: Customer with ID# {customer_id} set to active!')
  except Exception as e:
    print(f'\n- ERROR: {e}. Customer data was not updated. -')

def activate_all_customers():
  cursor.execute("UPDATE Customers SET active=True")
  connection.commit()

def activate_customer_option():
  are_inactive_customers = print_all_inactive_customers()
  if are_inactive_customers:
    customer_choice = input("\nEnter a Customer ID to Activate that Customer\nPress 'Enter' to return to Main Menu\n>>>")
    customer_info = get_customer_info(customer_choice, False)
    if customer_info:
      activate_customer(customer_choice)
    elif customer_choice == '':
      pass
    else:
      print('\n- ERROR: Invalid Customer ID. Returning to the Main Menu. -')
      

def deactivate_customer(id, name):
  while True:
    really_deactivate = input(f'\nAre you SURE you want to Deactivate Customer {id}:"{name}" (Y/N)? ')
    if really_deactivate.lower() == 'y':
      sql_deactivate = f"UPDATE Customers SET active=False WHERE customer_id=?"
      cursor.execute(sql_deactivate, (id,)).fetchone()
      connection.commit()
      print(f'SUCCESS: Customer "{name}" successfully Deactivated!')
      break
    elif really_deactivate.lower() != 'n':
      print('\n- ERROR: Invalid Response. Please try again. -')
    else:
      break

def check_for_active_column():
  try:
    rows = cursor.execute("SELECT active FROM Customers").fetchone()
    return True
    # if rows[0][0] == None:
    #   return False
    # else:
    #   return True
  except:
    return False
  
def add_active_column():
  cursor.execute('ALTER TABLE Customers ADD active int')

if not check_for_active_column():
  add_active_column()
  activate_all_customers()

while True:
  choice = input('\n**** Customer Database ****\n\n[1] View All Active Customers\n[2] Search Active Customers\n[3] Add a New Customer\n[4] Activate a Customer\n[Q] Quit\n\n>>>')
  if choice == '1':
    view_customers_option()
  elif choice == '2':
    search_customers_option()
  elif choice == '3':
    add_customer_option()
  elif choice == '4':
    activate_customer_option()
  elif choice.lower() == 'q':
    break
  else:
    print('\n- Please enter a valid choice from 1-4, or enter Q to quit. -')