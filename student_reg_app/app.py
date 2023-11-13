# To Start:
# python3 -m pipenv shell
# cd <directory>
# python3 app.py
import sqlite3
connection = sqlite3.connect('school_database.db')
cursor = connection.cursor()

# Create a Person record
def create_person():
  print('\nPlease fill out the form below to add a new Person:\n')
  field_choices = []
  field_choices.append(input(f"{'First Name:':>9} "))
  field_choices.append(input(f"{'Last Name:':>9} "))
  field_choices.append(input(f"{'Email:':>9} "))
  field_choices.append(input(f"{'Phone:':>9} "))
  field_choices.append(input(f"{'Password:':>9} "))
  field_choices.append(input(f"{'Address:':>9} "))
  field_choices.append(input(f"{'City:':>9} "))
  field_choices.append(input(f"{'State:':>9} "))
  field_choices.append(input(f"{'Zipcode:':>9} "))

  insert_sql = "INSERT INTO People (first_name, last_name, email, phone, password, address, city, state, postal_code, active) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, True)"
  try:
    cursor.execute(insert_sql, field_choices)
    connection.commit()
    print(f'\nSUCCESS: Person "{field_choices[0]} {field_choices[1]}" Successfully added!')
  except Exception as e:
    print(f'\n- ERROR: {e}. Customer was not added. -')

# Create a Course record (A course is a Class)
def create_course():
  print('Create Course!')

# Create a Cohort. The user must select:
# A. an existing Person as an instructor
# B. an existing Course as the course'
def create_cohort():
  print('Create Cohort!')

# Assign a Student to a Cohort. The user must select:
# A. An existing Person as the student
# B. An existing Cohort as the cohort
def assign_to_cohort():
  print('Assign to Cohort!')

# Remove a Student from a Cohort
# A. This should just set the Student_Cohort_Registration record as active = 0 AND set the drop_date to today
def remove_from_cohort():
  print('Remove from Cohort!')


# Deactivate a Course (It can no longer be selected for a new Cohort)\
def deactivate_course():
  print('Deactivate Course!')


# Deactivate a Person (They can no longer be selected for new Registrations or as an instructor for a Cohort)
def deactivate_person(id, first_name, last_name):
  while True:
    really_deactivate = input(f'\nAre you SURE you want to Deactivate Person {id}:"{first_name} {last_name}" (Y/N)? ')
    if really_deactivate.lower() == 'y':
      sql_deactivate = f"UPDATE People SET active=False WHERE person_id=?"
      cursor.execute(sql_deactivate, (id,)).fetchone()
      connection.commit()
      print(f'SUCCESS: "{first_name} {last_name}" successfully Deactivated!')
      break
    elif really_deactivate.lower() != 'n':
      print('\n- ERROR: Invalid Response. Please try again. -')
    else:
      break


# Deactivate a Cohort (They can no longer be selected for new student registrations)
def deactivate_cohort():
  print('Deactivate Cohort!')


# Complete a Course for a Student. This will set the completion date on the Student_Cohort_Registration.
def complete_course():
  print('Complete Course!')

# Reactivate Course, Person, Cohort, Student_Cohort_Registration
def reactivate_course():
  print('Reactivate Course!')

def reactivate_person():
  print('Reactivate Person!')

def reactivate_cohort():
  print('Reactivate Cohort!')

def reactivate_student_cohort_registration():
  print('Reactivate Student Cohort!')

# View active registrations for a cohort
def view_active_cohort_registrations():
  print('View Active Cohort Registrations!')

# View active cohorts for a course
def view_active_course_cohorts():
  print('View Active Courses!')

def get_all_active_people():
  try:
    rows = cursor.execute("SELECT person_id, first_name, last_name, city, state, phone, email FROM People WHERE active=True").fetchall()
    return rows
  except Exception as e:
    print(f'\n- ERROR: {e}. Customer data could not be loaded. -')

def get_person_info(id, active):
  try:
    person_info = cursor.execute("SELECT person_id, first_name, last_name, address, city, state, postal_code, phone, email, password FROM People WHERE person_id=? AND active=?", (id, active)).fetchone()
    return person_info
  except Exception as e:
    print(f'\n- ERROR: {e}. Could not retrieve customer information. -')
    return None
  
def update_person_info(field_to_update, new_value, person_id, field_name):
  try:
    sql_update = f"UPDATE People SET {field_to_update}=? WHERE person_id=?"
    update_values = (new_value, person_id)
    cursor.execute(sql_update, update_values)
    connection.commit()
    print(f'SUCCESS: {field_name} updated!')
  except Exception as e:
    print(f'\n- ERROR: {e}. Person data was not updated. -')

# View all active people
def view_active_people():
  print('\n--- People ---')
  rows = get_all_active_people()
  print(f'{"id":<2} {"First Name":<12} {"Last Name":<12} {"City":<20} {"State":<10} {"Phone":<15} {"Email":<25}')
  for row in rows:
    row_data = []
    for i in range(len(row)):
      if row[i]:
        row_data.append(row[i])
      else:
        row_data.append('None')
    try:
      print(f'{row_data[0]:<2} {row_data[1]:<12} {row_data[2]:<12} {row_data[3]:<20} {row_data[4]:<10} {row_data[5]:<15} {row_data[6]:<25}')
    except Exception as e:
      print(f'\n- ERROR: {e}. Could not print row data for customer -')

  select_person()

def select_person():
  person_choice = input("\nEnter a Person ID to View the Person's information\nPress 'Enter' to return to Main Menu\n>>>")
  while True:
    person_info = get_person_info(person_choice, True)
    if person_info:
      continue_loop = update_choice(person_info, person_choice)
      if not continue_loop:
        break
    elif person_choice == '':
      break
    else:
      print('\n- ERROR: Invalid Person ID. Returning to the Previous Menu. -')
      break

def print_person_details(person_info):
  if person_info:
    print('\n+++ Person Details +++\n')
    print(f"{'ID:':>9} {person_info[0]}")
    print(f"{'First Name:':>9} {person_info[1]}")
    print(f"{'Last Name:':>9} {person_info[2]}")
    print(f"{'Address:':>9} {person_info[3]}")
    print(f"{'City:':>9} {person_info[4]}")
    print(f"{'State:':>9} {person_info[5]}")
    print(f"{'Zipcode:':>9} {person_info[6]}")
    print(f"{'Phone:':>9} {person_info[7]}")
    print(f"{'Email:':>9} {person_info[8]}")
    # print(f"{'Password:':>9} {person_info[9]}")
  else:
    print('\n--- Invalid customer ID. Please try again ---')

# person_id, first_name, last_name, address, city, state, postal_code, phone, email, password

def update_choice(person_info, person_choice):
  pass
  if person_info:
    print_person_details(person_info)
    person_id, person_first_name, person_last_name, person_address, person_city, person_state, person_zipcode, person_phone, person_email, person_password = person_info
    edit_person_choice = input("\nTo update a field, enter the first letter of the field.\nTo change the person's password, type 'PASSWORD'\nTo deactivate this record, type 'DEACTIVATE'\nTo return to the previous menu, press 'Enter'.\n>>>")
    if edit_person_choice.lower() == 'i':
      print('\nThe ID cannot be changed.')
    elif edit_person_choice.lower() == 'f':
      print(f'\nCurrent First Name: {person_first_name}')
      new_first_name = input('New First Name: ')
      update_person_info('first_name', new_first_name, person_choice, 'First Name')
    elif edit_person_choice.lower() == 'l':
      print(f'\nCurrent Last Name: {person_last_name}')
      new_last_name = input('New Last Name: ')
      update_person_info('last_name', new_last_name, person_choice, 'Last Name')
    elif edit_person_choice.lower() == 'a':
      print(f'\nCurrent Address: {person_address}')
      new_address = input('New Address: ')
      update_person_info('street_address', new_address, person_choice, 'Address')
    elif edit_person_choice.lower() == 'c':
      print(f'\nCurrent City: {person_city}')
      new_city = input('New City: ')
      update_person_info('city', new_city, person_choice, 'City')
    elif edit_person_choice.lower() == 's':
      print(f'\nCurrent State: {person_state}')
      new_state = input('New State: ')
      update_person_info('state', new_state, person_choice, 'State')
    elif edit_person_choice.lower() == 'z':
      print(f'\nCurrent Zipcode: {person_zipcode}')
      new_zipcode = input('New Zipcode: ')
      update_person_info('postal_code', new_zipcode, person_choice, 'Zipcode')
    elif edit_person_choice.lower() == 'p':
      print(f'\nCurrent Phone Number: {person_phone}')
      new_phone_number = input('New Phone Number: ')
      update_person_info('phone', new_phone_number, person_choice, 'Phone Number')
    elif edit_person_choice.lower() == 'e':
      print(f'\nCurrent Email: {person_email}')
      new_email = input('New Email: ')
      update_person_info('email', new_email, person_choice, 'Email')
    elif edit_person_choice.lower() == 'password':
      password_guess = input("Please input the person's current password: ")
      if password_guess == person_password:
        print(f'\nCurrent Password: {person_password}')
        new_password = input('New Password: ')
        update_person_info('password', new_password, person_choice, 'Password')
      else:
        print('- Sorry, that password was incorrect. Please try again. -')
    elif edit_person_choice.lower() == 'deactivate':
      deactivate_person(person_id, person_first_name, person_last_name)
      return False
    elif edit_person_choice == '':
      return False
    else:
      print('- Invalid selection. Please try again. -')
    return True

# def print_all_inactive_customers():
#   rows = get_all_inactive_customers()
#   if rows:
#     print('\n--- Inactive Customers ---')
#     print(f'{"id":<2} {"Name":<25} {"City":<20} {"State":<10} {"Phone":<15} {"Email":<25}')
#     for row in rows:
#       row_data = []
#       for i in range(len(row)):
#         if row[i]:
#           row_data.append(row[i])
#         else:
#           row_data.append('None')
#       try:
#         print(f'{row_data[0]:<2} {row_data[1]:<25} {row_data[2]:<20} {row_data[3]:<10} {row_data[4]:<15} {row_data[5]:<25}')
#       except Exception as e:
#         print(f'\n- ERROR: {e}. Could not print row data for customer -')
#     return True
#   else:
#     print(f'\n- There are currently no Inactive Customers -')
#     return False

# Any other views you think might be helpful to the user.

main_menu = {
  
  "\n*** Welcome to School University's Student Registration App! ***\n\n1. Student and Teacher Menu": {
    '\n--- Student and Teacher Menu ---\n\n1. View Active People': view_active_people,
    '2. Register a Person': create_person,
    '3. Reactivate a Person': reactivate_person
  },
  '2. Cohort Menu': {
    '\n--- Cohort Menu ---\n1. View Active Cohorts': view_active_cohort_registrations,
    '2. Register a Cohort': create_cohort,
    '3. Reactivate a Cohort': reactivate_cohort
  },
  '3. Course Menu': {
    '\n--- Course Menu ---\n1. View Active Courses': view_active_course_cohorts,
    '2. Register a Course': create_course,
    '3. Reactivate a Course': reactivate_course
  }
}

def display_menu(menu):
  for key, value in menu.items():
    print(key)
  
def run_menu(menu):
  while True:
    is_main_menu = False
    menu_options = list(menu.keys())
    if menu_options[0][2] == '*':
      is_main_menu = True
    choices = ['1', '2', '3']
    actions = list(menu.values())
    display_menu(menu)
    choice = input("\nPlease choose an option from the menu above, 'q' to quit, or press 'enter' to return to the previous menu: ")
    if choice.lower() == 'q':
      print('\n - Goodbye! -')
      break
    elif choice == '' and not is_main_menu:
      return None
    elif choice == '' and is_main_menu:
      pass
    elif choice in choices:
      for i in range(len(choices)):
        if choices[i] == choice:
          if callable(actions[i]):
            actions[i]()
          else:
            run_menu(actions[i])
    else:
      print("\nSorry, I didn't understand your selection. Please enter a valid number from 1-3.")

run_menu(main_menu)