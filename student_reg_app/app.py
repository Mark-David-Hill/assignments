# To Start:
# python3 -m pipenv shell
# cd <directory>
# python3 app.py
import sqlite3
connection = sqlite3.connect('school_database.db')
cursor = connection.cursor()

# Create a Person record
def create_person():
  print('Create Person!')

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
def deactivate_person():
  print('Deactivate Person!')


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

# View all active people
print('View active people!')

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
    choice = input("\nPlease choose an option from the menu above, 'q' to quit, or press 'enter' to return to the main menu: ")
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