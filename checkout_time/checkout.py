def checkout_time(customers, n):
  
  total_minimum_time = 0
  temp_customers = customers
  while len(temp_customers) > 0:
    registers_in_use = 0
    if len(temp_customers) > n:
      registers_in_use = n
    else:
      registers_in_use = len(temp_customers)

    for i in range(registers_in_use):
      if i == 0:
        total_minimum_time += 1
      temp_customers[i] -= 1

    while 0 in customers:
      for i in range(len(customers)):
        if customers[i] == 0:
          customers.pop(i)
          break
      
  return total_minimum_time

print(checkout_time([5,3,4], 1) == 12) # 12
print(checkout_time([10,2,3,3], 2) == 10) # 10
print(checkout_time([2,3,10], 2) == 12) # 12
print(checkout_time([], 1) == 0) # 0
print(checkout_time([1,2,3,4], 1) == 10) # 10
print(checkout_time([2,2,3,3,4,4], 2) == 9) # 9
print(checkout_time([1,2,3,4,5], 100) == 5) # 5