import sqlite3

connection = sqlite3.connect('dp_customers.db')
cursor = connection.cursor()
rows = cursor.execute("SELECT name, price FROM Products WHERE make='Tenba'").fetchall()

def map_results(result_set, field_names_list):
  results_list = []
  for i in range(len(result_set)):
    results_list.append({})
    for j in range(len(field_names_list)):
      results_list[i][field_names_list[j]] = result_set[i][j]
  return results_list
      
columns = ['name', 'price']
results = map_results(rows, columns)

print(f'{"price":<9} {"name":<25}')
for row in results:
   print(f'{row["price"]:<9} {row["name"]:<25}')