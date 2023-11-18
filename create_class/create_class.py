import bcrypt
import sqlite3
connection = sqlite3.connect('user_database.db')
cursor = connection.cursor()

class User:
  def __init__(self, user_id, first_name, last_name, city, state, email, password, date_created, birth_month, birth_year):
    self.user_id = user_id
    self.first_name = first_name
    self.last_name = last_name
    self.city = city
    self.state = state
    self.email = email
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)
    self.password = hash
    self.date_created = date_created
    self.birth_month = birth_month
    self.birth_year = birth_year

  def change_password(self, new_password):
    bytes = new_password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)
    self.password = hash

  def check_password(self, user_password):
    try:
      user_bytes = user_password.encode('utf-8')
      result = bcrypt.checkpw(user_bytes, self.password)
      return result
    except Exception as e:
      print(f'ERROR: {e} Password Check could not be performed.')

  def update_email(self, new_email):
    self.email = new_email

  def print_details(self):
    print(f'user id: {self.user_id}')
    print(f'first name: {self.first_name}')
    print(f'last name: {self.last_name}')
    print(f'city: {self.city}')
    print(f'state: {self.state}')
    print(f'email: {self.email}')
    print(f'date created: {self.date_created}')
    print(f'birth month: {self.birth_month}')
    print(f'birth year: {self.birth_year}')
    print(f'password: {self.password}')

  def load(self, cursor, id_to_load = None):
    try:
      if id_to_load is None:
        id_to_load = self.user_id
      person_info = cursor.execute("SELECT user_id, first_name, last_name, city, state, email, password, date_created, birth_month, birth_year FROM Users WHERE user_id=?", (id_to_load, )).fetchone()
      self.user_id = person_info[0]
      self.first_name = person_info[1]
      self.last_name = person_info[2]
      self.city = person_info[3]
      self.state = person_info[4]
      self.email = person_info[5]
      self.password = person_info[6]
      self.date_created = person_info[7]
      self.birth_month = person_info[8]
      self.birth_year = person_info[9]
      print(f'\nSUCCESS: User "{self.first_name} {self.last_name}" Successfully loaded from the database!')
      return person_info
    except Exception as e:
      print(f'\n- ERROR: {e}. Could not Load User. -')
      return None

  def save(self, cursor):
    sql_select = 'SELECT first_name FROM Users WHERE user_id=?'
    record_exists = cursor.execute(sql_select, (self.user_id,)).fetchone()
    if record_exists:
      sql_update = "UPDATE Users SET user_id=?, first_name=?, last_name=?, city=?, state=?, email=?, password=?, date_created=?, birth_month=?, birth_year=? WHERE user_id=?"
      values = (self.user_id, self.first_name, self.last_name, self.city, self.state, self.email, self.password, self.date_created, self.birth_month, self.birth_year, self.user_id)
      try:
        cursor.execute(sql_update, values)
        connection.commit()
        print(f'\nSUCCESS: User "{self.first_name} {self.last_name}" Successfully saved to the database!')
      except Exception as e:
        print(f'\n- ERROR: {e}. User could not be saved. -')
    else:
      sql_insert = "INSERT INTO Users (user_id, first_name, last_name, city, state, email, password, date_created, birth_month, birth_year) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
      values = (self.user_id, self.first_name, self.last_name, self.city, self.state, self.email, self.password, self.date_created, self.birth_month, self.birth_year,)
      try:
        cursor.execute(sql_insert, values)
        connection.commit()
        print(f'\nSUCCESS: User "{self.first_name} {self.last_name}" Successfully saved to the database!')
      except Exception as e:
        print(f'\n- ERROR: {e}. User could not be saved. -')

# Example test code:
user = User(4, 'Rune', 'Hill', 'Eagle Mountain', 'The Amazon', 'rune@gmail.com', 'leaf_walking', '2023/11/17 12:12:12', 'April', 2023)
user.print_details()
user.save(cursor)
print(user.check_password('leaf_walking'))
print(user.check_password('incorrect_password'))
user.load(cursor, 1)
user.print_details()