
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}

student_grade = {}
for key,value in student_scores.items():
    if value > 90:
        student_grade[key] = "Outstanding"
    elif value > 80:
        student_grade[key] = "Exceeds Expectations"
    elif value > 70:
        student_grade[key] = "Acceptable"
    else:
        student_grade[key] = "Fail"

print(student_grade)
