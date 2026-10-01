students = {
    "Anna":[80,90,95],
    "John":[60,70,75],
    "Eva":[100,95,98]
}
def best_student(students):
    top_student = ""
    max_average = 0
    for student in students:
        average = sum(students[student]) / len(students[student])
        if average > max_average:
            max_average = average
            top_student = student
    return (top_student, round(max_average, 2))
print(best_student(students))