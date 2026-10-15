import os
file_name ="student_record"
student_name = "Ram"
student_marks = "200"

with open(file_name, 'w') as file:
  file.write(f"{student_name}\n")
  file.write(student_marks)
