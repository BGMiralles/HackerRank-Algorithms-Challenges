# Function Description:
#     Complete the function gradingStudents in the editor below.
#     gradingStudents has the following parameter(s):
#         int grades[n]: the grades before rounding
#
# Returns:
#     int[n]: the grades after rounding as appropriate
#
# Input Format:
#     The first line contains a single integer, `n`, the number of students.
#     Each line `i` of the `n` subsequent lines contains a single integer, grades[i].

import os


def gradingStudents(grades):
    grade = []
    for x in grades:
        if x < 38:
            grade.append(x)
        elif x >= 38:
            if x % 5 in range(0, 3):
                grade.append(x)
            elif x % 5 in range(3,5):
                grade.append(x + (5 - x % 5))
    return grade


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
