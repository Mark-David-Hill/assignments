def get_operator_str(str):
  operator = ''
  if str == 'lessthan':
    operator = '<'
  elif str == 'greaterthan':
    operator = '>'
  elif str == 'equals':
    operator = '='
  elif str == 'lessthanorequals':
    operator = '<='
  elif str == 'greaterthanorequals':
    operator = '>='
  elif str == 'LIKE':
    operator = 'LIKE'
  return operator

def to_sql(sql_dict):
  sql_str = 'SELECT '
  field_list = sql_dict['fields']
  for i in range(len(field_list)):
    if i < (len(field_list) - 1):
      sql_str += (field_list[i] + ', ')
    else:
      sql_str += (field_list[i] + ' ')

  sql_str += 'FROM '
  from_value = sql_dict['table']
  sql_str += from_value + ' '

  try:
    if sql_dict['where']['AND']:
      sql_str += 'WHERE '
      for i in range(len(sql_dict['where']['AND'])):
        if i > 0 and i < len(sql_dict['where']['AND']):
          sql_str += 'AND '
        where_clause = sql_dict['where']['AND'][i]
        sql_str += str(where_clause['field']) + ' '
        operator = str(where_clause['operator'])
        operator = get_operator_str(operator)
        sql_str += operator + ' '
        if type(where_clause['value']) is str:
          sql_str += ("'" + str(where_clause['value']) + "' ")
        else:
          sql_str += (f"{where_clause['value']:.2f}" + " ")
  except:
    pass
  try:
    if sql_dict['where']:
      sql_str += 'WHERE '
      where_clause = sql_dict['where']
      sql_str += str(where_clause['field']) + ' '
      operator = str(where_clause['operator'])
      operator = get_operator_str(operator)
      sql_str += operator + ' '
      if type(where_clause['value']) is str:
        sql_str += ("'" + str(where_clause['value']) + "' ")
      else:
        sql_str += (f"{where_clause['value']:.2f}" + " ")
  except:
    pass
    
  if sql_dict['order_by']:
    sql_str += 'ORDER BY '
    sql_str += sql_dict['order_by']['field'] + ' '
    if sql_dict['order_by']['order']:
      sql_str += sql_dict['order_by']['order']

  return sql_str

test_dict = {
   'fields': [
      'name', 
      'model', 
      'price'
   ],
   'table': 'Products',
   'where': {
      'AND': [
      	 {
            'field': 'make',
            'value': '%Apple%',
            'operator': 'LIKE'
         },
         {
            'field': 'price',
            'value': 1100.00,
            'operator': 'lessthan'
         }
      ]
   },
   'order_by': {
      'field': 'price',
      'order': 'DESC'
   },
   'limit': 0
}

expected_output = "SELECT name, model, price FROM Products WHERE make LIKE '%Apple%' AND price < 1100.00 ORDER BY price DESC"
test_output = to_sql(test_dict)
print(expected_output)
print(test_output)

test_dict = {'fields': ['name', 'model', 'price'], 'table': 'Products', 'where': {'field': 'make', 'value': '%Apple%', 'operator': 'lessthan'}, 'order_by': {'field': 'price', 'order': 'DESC'}, 'limit': 0}
test_output = to_sql(test_dict)
print(test_output)