
# Write a program to print the sum of all even numbers between 1 and 50.
even= []

for i in range(51):
  if i % 2 == 0:
    even.append(i)

print(f"{even}")

# sum 
# sum = 0
# for i in even:
#   sum = sum+i

# print("sum of even no up to 50 is",sum)

add = sum(even)
print(add)

# One-liner solution
# total = sum([i for i in range(51) if i % 2 == 0])
# print("Sum of even numbers up to 50 is", total)


total = sum([i for i in range(51) if i % 2 == 0])
print(total)