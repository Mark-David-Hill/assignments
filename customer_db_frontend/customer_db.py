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

def view_customers():
  print_all_customers()
  customer_choice = input("\nEnter a Customer ID to View a Customer\nPress 'Enter' to return to Main Menu\n>>>")
  was_valid_id = print_customer_details(customer_choice)
  if was_valid_id:
    edit_customer_choice = input("\nTo update a field, enter the first letter of the field. \nTo delete this record, type 'DELETE'\nTo return to the main menu, press 'Enter'.\n>>>")
  # Determine what to do based on choice, or break out of things

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