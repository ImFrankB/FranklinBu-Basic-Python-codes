student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

students_grade = {}

for name, x in student_scores.items():
    if x >=91 and x <=100:
        #dict          key  :   value 
        students_grade[name] = "Outstanding"
    elif x >=81 and x <= 90:
        students_grade[name] = "Exceeds expectations"
    elif x>= 71 and x <=80:
        students_grade[name] = "Acceptable"
    else:
        students_grade[name] = "Fail"


print(students_grade)