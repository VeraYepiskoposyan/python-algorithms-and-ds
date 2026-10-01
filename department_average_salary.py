def department_average(employees):
    if not employees:
        return None

    tracker = {}
    for name, department, salary in employees:
        if department not in tracker:
            tracker[department] = [salary, 1]
        else:
            tracker[department][0] += salary
            tracker[department][1] += 1
    result = {}
    for department in tracker:
        total_salary = tracker[department][0]
        count = tracker[department][1]
        average_salary = total_salary / count
        result[department] = average_salary
    return result
print(department_average(employees = [
    ("Anna","IT",4000),
    ("John","HR",3000),
    ("Eva","IT",4500),
    ("Tom","Sales",3500)
]))



