import random
no_list =[]


for i in range(10):

  rand_no = random.randint(1,100)
  no_list.append(rand_no)



print(no_list)


print(set(no_list))