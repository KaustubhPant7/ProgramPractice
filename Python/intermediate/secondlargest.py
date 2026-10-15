import random
number_list = []

for i in range (11):
  random_no = random.randint(1,10)
  number_list.append(random_no)

print(number_list)

max_no = max(number_list)
print(max_no)