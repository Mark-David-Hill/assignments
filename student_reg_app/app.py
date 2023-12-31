# To Start:
# python3 -m pipenv shell
# cd <directory>
# python3 app.py
from datetime import datetime
import sqlite3
connection = sqlite3.connect('school_database.db')
cursor = connection.cursor()

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
    print(f'\n- ERROR: {e}. Person was not added. -')

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

def reactivate_person(person_id):
  try:
    sql_update = f"UPDATE People SET active=True WHERE person_id=?"
    update_values = (person_id,)
    cursor.execute(sql_update, update_values)
    connection.commit()
    print(f'\nSUCCESS: Person with ID# {person_id} set to active!')
  except Exception as e:
    print(f"\n- ERROR: {e}. Person's data was not updated. -")

def reactivate_person_option():
  are_inactive_people = view_inactive_people()
  if are_inactive_people:
    person_choice = input("\nEnter a Person's ID to Activate that Person\nPress 'Enter' to return to the previous menu\n>>>")
    person_info = get_person_info(person_choice, False)
    if person_info:
      reactivate_person(person_choice)
    elif person_choice == '':
      pass
    else:
      print('\n- ERROR: Invalid Person ID. Returning to the previous menu. -')

def get_all_active_people():
  try:
    rows = cursor.execute("SELECT person_id, first_name, last_name, city, state, phone, email FROM People WHERE active=True").fetchall()
    return rows
  except Exception as e:
    print(f'\n- ERROR: {e}. Person data could not be loaded. -')

def get_all_inactive_people():
  try:
    rows = cursor.execute("SELECT person_id, first_name, last_name, city, state, phone, email FROM People WHERE active=False").fetchall()
    return rows
  except Exception as e:
    print(f'\n- ERROR: {e}. Person data could not be loaded. -')

def get_person_info(id, active):
  try:
    person_info = cursor.execute("SELECT person_id, first_name, last_name, address, city, state, postal_code, phone, email, password FROM People WHERE person_id=? AND active=?", (id, active)).fetchone()
    return person_info
  except Exception as e:
    print(f'\n- ERROR: {e}. Could not retrieve person information. -')
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

def view_active_people():
  print('\n--- People ---')
  rows = get_all_active_people()
  if rows:
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
        print(f'\n- ERROR: {e}. Could not print row data for person -')
  else:
    print(f'\n- There are currently no Active People -')
    return False

def view_active_people_and_update():
  print('\n--- People ---')
  rows = get_all_active_people()
  if rows:
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
        print(f'\n- ERROR: {e}. Could not print row data for person -')
    select_person()
  else:
    print(f'\n- There are currently no Active People -')
    return False

def view_inactive_people():
  rows = get_all_inactive_people()
  if rows:
    print('\n--- Inactive People ---')
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
        print(f'\n- ERROR: {e}. Could not print row data for person -')
    return True
  else:
    print(f'\n- There are currently no Inactive People -')
    return False
  
def select_person():
  person_choice = input("\nEnter a Person ID to View the Person's information\nPress 'Enter' to the previous menu\n>>>")
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
    print('\n--- Invalid person ID. Please try again ---')

def update_choice(person_info, person_choice):
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


def create_course():
  try:
    print('\nPlease fill out the form below to add a new Course:\n')
    field_choices = []
    field_choices.append(input(f"{'Course Name:':>9} "))
    field_choices.append(input(f"{'Course Description:':>9} "))
    insert_sql = "INSERT INTO Courses (name, description, active) VALUES (?, ?, True)"
    cursor.execute(insert_sql, field_choices)
    connection.commit()
    print(f'\nSUCCESS: Course "{field_choices[0]}" Successfully added!')
  except Exception as e:
    print(f'\n- ERROR: {e}. Course was not added. -')
  

def deactivate_course(id, name):
  while True:
    really_deactivate = input(f'\nAre you SURE you want to Deactivate Course {id}:"{name}" (Y/N)? ')
    if really_deactivate.lower() == 'y':
      sql_deactivate = f"UPDATE Courses SET active=False WHERE course_id=?"
      cursor.execute(sql_deactivate, (id,)).fetchone()
      connection.commit()
      print(f'SUCCESS: "{name}" successfully Deactivated!')
      break
    elif really_deactivate.lower() != 'n':
      print('\n- ERROR: Invalid Response. Please try again. -')
    else:
      break

def reactivate_course(id):
  try:
    sql_update = f"UPDATE Courses SET active=True WHERE course_id=?"
    update_values = (id,)
    cursor.execute(sql_update, update_values)
    connection.commit()
    print(f'\nSUCCESS: Course with ID# {id} set to active!')
  except Exception as e:
    print(f"\n- ERROR: {e}. Person's data was not updated. -")

def reactivate_course_option():
  are_inactive_courses = view_inactive_courses()
  if are_inactive_courses:
    course_choice = input("\nEnter a Course's ID to Activate that Course\nPress 'Enter' to return to the previous menu\n>>>")
    course_info = get_course_info(course_choice, False)
    if course_info:
      reactivate_course(course_choice)
    elif course_choice == '':
      pass
    else:
      print('\n- ERROR: Invalid Course ID. Returning to the previous menu. -')

def view_active_courses():
  print('\n--- Courses ---')
  rows = get_all_active_courses()
  if rows:
    print(f'{"id":<2} {"Name":<20} {"Description":<35}')
    for row in rows:
      row_data = []
      for i in range(len(row)):
        if row[i]:
          row_data.append(row[i])
        else:
          row_data.append('None')
      try:
        print(f'{row_data[0]:<2} {row_data[1]:<20} {row_data[2]:<35}')
      except Exception as e:
        print(f'\n- ERROR: {e}. Could not print row data for course -')
  else:
    print(f'\n- There are currently no Active Courses -')
    return False

def view_active_courses_and_deactivate():
  print('\n--- Courses ---')
  rows = get_all_active_courses()
  if rows:
    print(f'{"id":<2} {"Name":<20} {"Description":<35}')
    for row in rows:
      row_data = []
      for i in range(len(row)):
        if row[i]:
          row_data.append(row[i])
        else:
          row_data.append('None')
      try:
        print(f'{row_data[0]:<2} {row_data[1]:<20} {row_data[2]:<35}')
      except Exception as e:
        print(f'\n- ERROR: {e}. Could not print row data for course -')
  else:
    print(f'\n- There are currently no Active Courses -')
    return False
  deactivate_or_view_cohorts_for_course_prompt()

def get_all_active_courses():
  try:
    rows = cursor.execute("SELECT course_id, name, description FROM Courses WHERE active=True").fetchall()
    return rows
  except Exception as e:
    print(f'\n- ERROR: {e}. Course data could not be loaded. -')

def get_all_inactive_courses():
  try:
    rows = cursor.execute("SELECT course_id, name, description FROM Courses WHERE active=False").fetchall()
    return rows
  except Exception as e:
    print(f'\n- ERROR: {e}. Course data could not be loaded. -')

def get_course_info(id, active):
  try:
    course_info = cursor.execute("SELECT course_id, name, description FROM Courses WHERE course_id=? AND active=?", (id, active)).fetchone()
    return course_info
  except Exception as e:
    print(f'\n- ERROR: {e}. Could not retrieve course information. -')
    return None
  
def view_inactive_courses():
  rows = get_all_inactive_courses()
  if rows:
    print('\n--- Inactive Courses ---')
    print(f'{"id":<2} {"Name":<20} {"Description":<35}')
    for row in rows:
      row_data = []
      for i in range(len(row)):
        if row[i]:
          row_data.append(row[i])
        else:
          row_data.append('None')
      try:
        print(f'{row_data[0]:<2} {row_data[1]:<20} {row_data[2]:<35}')
      except Exception as e:
        print(f'\n- ERROR: {e}. Could not print row data for course -')
    return True
  else:
    print(f'\n- There are currently no Inactive Courses -')
    return False
  
def deactivate_or_view_cohorts_for_course_prompt():
  choice = input("\nTo View active Cohorts for a Course, type 'VIEW'\nTo deactivate a Course, type 'DEACTIVATE'\nTo return to the previous menu, press 'Enter'.\n>>>")
  if choice.lower() == 'view':
    course_choice = input("\nPlease enter the ID of the Course you would like to View active Cohorts for\nor press 'Enter' to return to the previous menu: ")
    course_info = get_course_info(course_choice, True)
    if course_info:
      view_specific_cohorts(course_choice)
      input("\nPress 'Enter' to Continue")
    elif course_choice == '':
      pass
    else:
      print('\n- ERROR: Invalid Course ID. Returning to the Previous Menu. -')
  elif choice.lower() == 'deactivate':
    course_choice = input("\nPlease enter the ID of the Course you would like to Deactivater\nor press 'Enter' to return to the previous menu: ")
    course_info = get_course_info(course_choice, True)
    if course_info:
      deactivate_course(course_info[0], course_info[1])
    elif course_choice == '':
      pass
    else:
      print('\n- ERROR: Invalid Course ID. Returning to the Previous Menu. -')
 

def deactivate_or_view_registrations_for_cohort_prompt():
  choice = input("\nTo View active registrations for a Cohort, type 'VIEW'\nTo deactivate a Cohort, type 'DEACTIVATE'\nTo return to the previous menu, press 'Enter'.\n>>>")
  if choice.lower() == 'view':
    cohort_choice = input("\nPlease enter the ID of the Cohort you would like to View active Registrations for\nor press 'Enter' to return to the previous menu: ")
    cohort_info = get_cohort_info(cohort_choice, True)
    if cohort_info:
      # ***** View Active registrations for selected cohort
      view_specific_cohort_registrations(cohort_choice)
      input("\nPress 'Enter' to Continue")
      pass
    elif cohort_choice == '':
      pass
    else:
      print('\n- ERROR: Invalid Course ID. Returning to the Previous Menu. -')
  elif choice.lower() == 'deactivate':
    cohort_choice = input("\nPlease enter the ID of the Cohort you would like to Deactivate\nor press 'Enter' to return to the previous menu: ")
    cohort_info = get_cohort_info(cohort_choice, True)
    if cohort_info:
      deactivate_cohort(cohort_choice, cohort_info[3])
    elif cohort_choice == '':
      pass
    else:
      print('\n- ERROR: Invalid Course ID. Returning to the Previous Menu. -')
  else:
    pass

def view_specific_cohorts(course_id):
  print('\n--- Cohorts ---')
  rows = get_all_active_cohorts(course_id)
  if rows:
    print(f'{"id":<2} {"Course":<18} {"Instructor":<18} {"Start Date":<24} {"End Date":<24}')
    for row in rows:
      row_data = []
      for i in range(len(row)):
        if row[i]:
          row_data.append(row[i])
        else:
          row_data.append('None')
      try:
        print(f'{row_data[0]:<2} {row_data[3]:<18} {row_data[1] + " " + row_data[2]:<18} {row_data[4]:<24} {row_data[5]:<24}')
      except Exception as e:
        print(f'\n- ERROR: {e}. Could not print row data for cohorts -')
  else:
    print(f'\n- There are currently no Active Cohorts -')
    return False

def view_active_cohorts(prompt_deactivation = True):
  print('\n--- Cohorts ---')
  rows = get_all_active_cohorts()
  if rows:
    print(f'{"id":<2} {"Course":<18} {"Instructor":<18} {"Start Date":<24} {"End Date":<24}')
    for row in rows:
      row_data = []
      for i in range(len(row)):
        if row[i]:
          row_data.append(row[i])
        else:
          row_data.append('None')
      try:
        print(f'{row_data[0]:<2} {row_data[3]:<18} {row_data[1] + " " + row_data[2]:<18} {row_data[4]:<24} {row_data[5]:<24}')
      except Exception as e:
        print(f'\n- ERROR: {e}. Could not print row data for cohorts -')
  else:
    print(f'\n- There are currently no Active Cohorts -')
    return False
  if prompt_deactivation == True:
    deactivate_or_view_registrations_for_cohort_prompt()

def view_inactive_cohorts():
  print('\n--- Cohorts ---')
  rows = get_all_inactive_cohorts()
  if rows:
    print(f'{"id":<2} {"Course":<18} {"Instructor":<18} {"Start Date":<24} {"End Date":<24}')
    for row in rows:
      row_data = []
      for i in range(len(row)):
        if row[i]:
          row_data.append(row[i])
        else:
          row_data.append('None')
      try:
        print(f'{row_data[0]:<2} {row_data[3]:<18} {row_data[1] + " " + row_data[2]:<18} {row_data[4]:<24} {row_data[5]:<24}')
      except Exception as e:
        print(f'\n- ERROR: {e}. Could not print row data for cohorts -')
    return True
  else:
    print(f'\n- There are currently no Active Cohorts -')
    return False

def get_all_active_cohorts(course_id = None):
  try:
    if course_id is None:
      rows = cursor.execute("SELECT c.cohort_id, p.first_name, p.last_name, cour.name, c.start_date, c.end_date FROM Cohorts c JOIN People p ON p.person_id = c.instructor_id JOIN Courses cour ON cour.course_id = c.course_id WHERE c.active=True").fetchall()
      return rows
    else:
      rows = cursor.execute("SELECT c.cohort_id, p.first_name, p.last_name, cour.name, c.start_date, c.end_date FROM Cohorts c JOIN People p ON p.person_id = c.instructor_id JOIN Courses cour ON cour.course_id = c.course_id WHERE c.active=True AND c.course_id=?",(course_id,)).fetchall()
      return rows
  except Exception as e:
    print(f'\n- ERROR: {e}. Cohort data could not be loaded. -')

def get_cohort_info(id, active):
  try:
    if id == '':
      return None
    row = cursor.execute("SELECT c.cohort_id, p.first_name, p.last_name, cour.name, c.start_date, c.end_date FROM Cohorts c JOIN People p ON p.person_id = c.instructor_id JOIN Courses cour ON cour.course_id = c.course_id WHERE c.cohort_id=? AND c.active=?", (id, active)).fetchone()
    return row
  except Exception as e:
    print(f'\n- ERROR: {e}. Cohort data could not be loaded. -')

def get_all_inactive_cohorts():
  try:
    rows = cursor.execute("SELECT c.cohort_id, p.first_name, p.last_name, cour.name, c.start_date, c.end_date FROM Cohorts c JOIN People p ON p.person_id = c.instructor_id JOIN Courses cour ON cour.course_id = c.course_id WHERE c.active=False").fetchall()
    return rows
  except Exception as e:
    print(f'\n- ERROR: {e}. Cohort data could not be loaded. -')

def create_cohort():
  try:
    print('\nPlease fill out the form below to add a new Cohort:\n')
    field_choices = []
    view_active_people()
    field_choices.append(input('\nPlease enter the id of the person you would like to be the Cohort Instructor: '))
    view_active_courses()
    field_choices.append(input('\nPlease enter the id of the course you would like to create a Cohort for: '))
    current_date_time = datetime.now()
    date_str = current_date_time.strftime("%Y/%m/%d %H:%M:%S")
    field_choices.append(date_str)
    field_choices.append(input('\nPlease enter the end date for this course (YYYY-MM-DD hh:mm:ss): '))

    insert_sql = "INSERT INTO Cohorts (instructor_id, course_id, start_date, end_date, active) VALUES (?, ?, ?, ?, True)"
    try:
      cursor.execute(insert_sql, field_choices)
      connection.commit()
      print(f'\nSUCCESS: Cohort Successfully added!')
    except Exception as e:
      print(f'\n- ERROR: {e}. Cohort was not added. -')
  except Exception as e:
      print(f'\n- ERROR: {e}. Cohort was not added. -')

def deactivate_cohort(id, cohort_name):
  while True:
    really_deactivate = input(f'\nAre you SURE you want to Deactivate Cohort {id}:"{cohort_name}" (Y/N)? ')
    if really_deactivate.lower() == 'y':
      sql_deactivate = f"UPDATE Cohorts SET active=False WHERE cohort_id=?"
      cursor.execute(sql_deactivate, (id,)).fetchone()
      connection.commit()
      print(f'SUCCESS: "{cohort_name}" Cohort successfully Deactivated!')
      break
    elif really_deactivate.lower() != 'n':
      print('\n- ERROR: Invalid Response. Please try again. -')
    else:
      break

def reactivate_cohort(cohort_id):
  try:
    sql_update = f"UPDATE Cohorts SET active=True WHERE cohort_id=?"
    update_values = (cohort_id,)
    cursor.execute(sql_update, update_values)
    connection.commit()
    print(f'\nSUCCESS: Cohort with ID# {cohort_id} set to active!')
  except Exception as e:
    print(f"\n- ERROR: {e}. Cohort's data was not updated. -")

def reactivate_cohort_option():
  are_inactive_cohorts = view_inactive_cohorts()
  if are_inactive_cohorts:
    cohort_choice = input("\nEnter a Cohort's ID to Activate that Cohort\nPress 'Enter' to return to the previous menu\n>>>")
    cohort_info = get_cohort_info(cohort_choice, False)
    if cohort_info:
      reactivate_cohort(cohort_choice)
    elif cohort_choice == '':
      pass
    else:
      print('\n- ERROR: Invalid Cohort ID. Returning to the previous menu. -')


def assign_to_cohort(cohort_id, person_id, person_name):
  try:
    get_cohort_info(cohort_id, True)
    really_register = input(f'Are you sure you want to register {person_name} to Cohort #{cohort_id}? (Y/N): ')
    if really_register.lower() == 'y':
      current_date_time = datetime.now()
      date_str = current_date_time.strftime("%Y/%m/%d %H:%M:%S")
      values = [person_id, cohort_id, date_str]
      insert_sql = "INSERT INTO Student_Cohort_Registrations (student_id, cohort_id, registration_date, active) VALUES (?, ?, ?, True)"
      cursor.execute(insert_sql, values)
      connection.commit()
      print(f'\nSUCCESS: Person "{person_name}" Successfully registered!')
    elif really_register.lower() != 'n':
      print('Invalid choice. Please try again.')
  except Exception as e:
    print(f'\n- ERROR: {e}. Registration was not completed. -')

def remove_from_cohort(cohort_id, student_id, first_name, last_name):
  while True:
      student_name = first_name + ' ' + last_name
      really_remove = input(f'\nAre you SURE you want to Remove "{student_name}" from Cohort ID {cohort_id} (Y/N)? ')
      if really_remove.lower() == 'y':
        current_date_time = datetime.now()
        date_str = current_date_time.strftime("%Y/%m/%d %H:%M:%S")
        sql_remove = f"UPDATE Student_Cohort_Registrations SET active=False, drop_date=? WHERE cohort_id=? AND student_id=?"
        cursor.execute(sql_remove, (date_str, cohort_id, student_id,)).fetchone()
        connection.commit()
        print(f'SUCCESS: "{student_name}" was Removed from Cohort ID {cohort_id}!')
        break
      elif really_remove.lower() != 'n':
        print('\n- ERROR: Invalid Response. Please try again. -')
      else:
        break

def get_all_active_cohort_registrations(cohort_id = None):
  try:
    if cohort_id is None:
      rows = cursor.execute("SELECT r.cohort_id, p.first_name, p.last_name, r.registration_date, r.completion_date, r.drop_date, r.student_id FROM Student_Cohort_Registrations r JOIN People p ON r.student_id=p.person_id WHERE r.active=True").fetchall()
      return rows
    else:
      rows = cursor.execute("SELECT r.cohort_id, p.first_name, p.last_name, r.registration_date, r.completion_date, r.drop_date, r.student_id FROM Student_Cohort_Registrations r JOIN People p ON r.student_id=p.person_id WHERE r.active=True AND r.cohort_id=?", (cohort_id,)).fetchall()
      return rows
  except Exception as e:
    print(f'\n- ERROR: {e}. Registration data could not be loaded. -')

def get_all_inactive_cohort_registrations():
  try:
    rows = cursor.execute("SELECT r.cohort_id, p.first_name, p.last_name, r.registration_date, r.completion_date, r.drop_date, r.student_id FROM Student_Cohort_Registrations r JOIN People p ON r.student_id=p.person_id WHERE r.active=False").fetchall()
    return rows
  except Exception as e:
    print(f'\n- ERROR: {e}. Registration data could not be loaded. -')

def get_cohort_registration_info(cohort_id, student_id, active):
  try:
    row = cursor.execute("SELECT r.cohort_id, r.student_id, p.first_name, p.last_name, r.registration_date, r.completion_date, r.drop_date FROM Student_Cohort_Registrations r JOIN People p ON r.student_id=p.person_id WHERE r.cohort_id=? AND r.student_id=? AND r.active=True", (cohort_id, student_id,)).fetchone()
    return row
  except Exception as e:
    print(f'\n- ERROR: {e}. Cohort data could not be loaded. -')

def remove_from_or_complete_cohort_prompt():
  choice = input("\nTo Complete a course for a student, type 'Complete'\nTo Remove a student from a cohort, type 'Remove'\nTo return to the previous menu, press 'Enter'.\n>>>")
  if choice.lower() == 'complete':
    print('\nPlease fill out the form below:')
    cohort_id = input("Cohort ID: ")
    student_id = input("Student ID: ")
    registration_info = get_cohort_registration_info(cohort_id, student_id, True)
    try:
      complete_course(registration_info[0], registration_info[1], registration_info[2], registration_info[3])
    except:
      print('\n- ERROR: Incorrect ID combination. Could not remove registration. -')
  elif choice.lower() == 'remove':
    print('\nPlease fill out the form below:')
    cohort_id = input("Cohort ID: ")
    student_id = input("Student ID: ")
    registration_info = get_cohort_registration_info(cohort_id, student_id, True)
    try:
      remove_from_cohort(registration_info[0], registration_info[1], registration_info[2], registration_info[3])
    except:
      print('\n- ERROR: Incorrect ID combination. Could not remove registration. -')

def complete_course(cohort_id, student_id, first_name, last_name):
  while True:
      student_name = first_name + ' ' + last_name
      really_remove = input(f'\nAre you SURE you want to mark the student "{student_name}" as having completed the class as part of Cohort ID {cohort_id} (Y/N)? ')
      if really_remove.lower() == 'y':
        current_date_time = datetime.now()
        date_str = current_date_time.strftime("%Y/%m/%d %H:%M:%S")
        sql_remove = f"UPDATE Student_Cohort_Registrations SET completion_date=? WHERE cohort_id=? AND student_id=?"
        cursor.execute(sql_remove, (date_str, cohort_id, student_id,)).fetchone()
        connection.commit()
        print(f'SUCCESS: "{student_name}" successfully completed the course as part of Cohort ID {cohort_id}!')
        break
      elif really_remove.lower() != 'n':
        print('\n- ERROR: Invalid Response. Please try again. -')
      else:
        break





def reactivate_cohort_registration(cohort_id, person_id):
  try:
    sql_update = f"UPDATE Student_Cohort_Registrations SET active=True, drop_date='None' WHERE cohort_id=? AND student_id=?"
    update_values = (cohort_id, person_id,)
    cursor.execute(sql_update, update_values)
    connection.commit()
    print(f'\nSUCCESS: Registration with Student ID# {person_id} and Cohort ID# {cohort_id} set to active!')
  except Exception as e:
    print(f"\n- ERROR: {e}. Cohort Registration was not reactivated. -")

def reactivate_cohort_registration_option():
  are_inactive_cohort_registrations = view_cohort_registrations(False)
  if are_inactive_cohort_registrations:
    print('\nTo reactivate a cohort registration, please fill out the form below with the data from your chosen registration:')
    cohort_id = input("Cohort ID: ")
    student_id = input("Student ID: ")
    try:
      reactivate_cohort_registration(cohort_id, student_id)
    except:
      print('\n- ERROR: Incorrect ID combination. Could not remove registration. -')
  else:
    print('\n- ERROR: There are no inactive Cohort Registrations. Returning to the previous menu. -')


def view_cohort_registrations(active = True):
  print('\n--- Cohort Registrations ---')
  rows = None
  if active:
    rows = get_all_active_cohort_registrations()
  else:
    rows = get_all_inactive_cohort_registrations()
  if rows:
    print(f'{"Cohort ID":<11} {"Student ID":<11} {"Student Name":<18} {"Registration Date":<24} {"Completion Date":<24} {"Drop Date":<24}')
    for row in rows:
      row_data = []
      for i in range(len(row)):
        if row[i]:
          row_data.append(row[i])
        else:
          row_data.append('None')
      try:
        print(f'{row_data[0]:<11} {row_data[6]:<11} {row_data[1] + " " + row_data[2]:<18} {row_data[3]:<24} {row_data[4]:<24} {row_data[5]:<24}')
      except Exception as e:
        print(f'\n- ERROR: {e}. Could not print row data for cohorts -')
  else:
    print(f'\n- There are currently no Active Cohorts -')
    return False
  if active:
    remove_from_or_complete_cohort_prompt()
  else:
    return True
  
def view_specific_cohort_registrations(cohort_id):
  print('\n--- Cohort Registrations ---')
  rows = get_all_active_cohort_registrations(cohort_id)
  if rows:
    print(f'{"Cohort ID":<11} {"Student ID":<11} {"Student Name":<18} {"Registration Date":<24} {"Completion Date":<24} {"Drop Date":<24}')
    for row in rows:
      row_data = []
      for i in range(len(row)):
        if row[i]:
          row_data.append(row[i])
        else:
          row_data.append('None')
      try:
        print(f'{row_data[0]:<11} {row_data[6]:<11} {row_data[1] + " " + row_data[2]:<18} {row_data[3]:<24} {row_data[4]:<24} {row_data[5]:<24}')
      except Exception as e:
        print(f'\n- ERROR: {e}. Could not print row data for cohorts -')
  else:
    print(f'\n- There are currently no Active Cohorts -')
    return False


def register_student_option():
  try:
    view_active_people()
    print('\nTo register a student to a cohort, please fill out the form below:')
    student_id = input("\nStudent ID: ")
    student_info = get_person_info(student_id, True)
    student_first_name = student_info[1]
    student_last_name = student_info[2]
    view_active_cohorts(False)
    cohort_id = input("\nCohort ID: ")
    student_name = student_first_name + ' ' + student_last_name
    assign_to_cohort(cohort_id, student_id, student_name)
    return False
  except Exception as e:
    print(f'\n- Error: {e} Unable to complete student registration to cohort. -')


main_menu = {
  
  "\n*** Welcome to School University's Student Registration App! ***\n\n1. Student and Teacher Menu": {
    '\n--- Student and Teacher Menu ---\n\n1. View Active People': view_active_people_and_update,
    '2. Register a Person': create_person,
    '3. Reactivate a Person': reactivate_person_option
  },
  '2. Course Menu': {
    '\n--- Course Menu ---\n\n1. View Active Courses': view_active_courses_and_deactivate,
    '2. Register a Course': create_course,
    '3. Reactivate a Course': reactivate_course_option
  },
  '3. Cohort Menu': {
    '\n--- Cohort Menu ---\n\n1. View Active Cohorts': view_active_cohorts,
    '2. Register a Cohort': create_cohort,
    '3. Reactivate a Cohort': reactivate_cohort_option
  },
  '4. Student Cohort Registration Menu': {
    '\n--- Student Cohort Registration Menu ---\n\n1. View Active Cohort Registrations': view_cohort_registrations,
    '2. Register Student to Cohort': register_student_option,
    '3. Reactivate Cohort Registration': reactivate_cohort_registration_option
  }
}

def display_menu(menu):
  for key, value in menu.items():
    print(key)
  
def run_menu(menu):
  quit_pending = False
  while True:
    is_main_menu = False
    menu_options = list(menu.keys())
    if menu_options[0][2] == '*':
      is_main_menu = True
    choices = []
    for i in range(len(menu_options)):
      choices.append(str(i + 1))
    actions = list(menu.values())
    display_menu(menu)
    choice = input("\nPlease choose an option from the menu above, 'q' to quit, or press 'Enter' to return to the previous menu: ")
    if choice.lower() == 'q':
      print('\n - Goodbye! -')
      return True
    elif choice == '' and not is_main_menu:
      return False
    elif choice == '' and is_main_menu:
      pass
    elif choice in choices:
      for i in range(len(choices)):
        if choices[i] == choice:
          if callable(actions[i]):
            actions[i]()
          else:
            quit_pending = run_menu(actions[i])
    else:
      print("\nSorry, I didn't understand your selection. Please enter a valid option.")
    if quit_pending == True:
      break

run_menu(main_menu)