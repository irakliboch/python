# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
sum_student_heights = 0
sum_number_of_people = 0

for heights in student_heights:
  sum_student_heights += int(heights)

for heights in student_heights:
  sum_number_of_people += 1

average_height = sum_student_heights / sum_number_of_people

print(round(average_height))





#average_size = sum(student_heights) / len(student_heights)

#print(average_size)
