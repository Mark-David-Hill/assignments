def view_customers():
  print('--- Customers ---')

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