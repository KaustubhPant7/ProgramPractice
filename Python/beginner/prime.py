# Write a program to check if a given number is prime.

while True:
  try:
    number = int(input("enter your no: "))
    break
  except ValueError:
    print("invalid Input\n")

count = 0
for i in range(1,number+1):
  print("this is",i)
  if(number % i  == 0):
    count =count+1
    


if count == 2:
  print("Prime")
else:
  print("not Prime")