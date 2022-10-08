
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0 

for i in student_heights:
    total_height+=i

total_students=0

for x in student_heights:
    total_students+=1

average_height = total_height/total_students

print(f"The average height is {average_height}")
