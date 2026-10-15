# Take a string input and count how many vowels it contains.
str = input("enter your string")

count = 0
for leteter in str:
  if leteter == 'a' or leteter == 'e' or leteter == 'i' or leteter == 'o' or leteter == 'u':
    count = count + 1


print (count)