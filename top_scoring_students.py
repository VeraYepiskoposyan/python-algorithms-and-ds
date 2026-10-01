students = [
    ("Anna", 82),
    ("John", 95),
    ("Eva", 76),
    ("Mark", 95),
    ("Tom", 60)
]
def highest_students(students):
    highest_score = students[0][1]
    top_students = []
    for student, score in students:
        if score > highest_score:
            highest_score = score
            top_students = [student]
        elif score == highest_score:
            top_students.append(student)
    return top_students
print(highest_students(students))