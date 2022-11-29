# calculate the average student height from a List of heights.
# student_heights


student_heights = input("Input a list of student heights. ")
height_list = student_heights.split()

height_sum = 0
student_number = 0
for height in height_list:
    height_sum+=int(height)
    student_number += 1
    average = round(height_sum/student_number)

print(f"The total student number is {student_number}.")
print(f"The average height is {average}.")
