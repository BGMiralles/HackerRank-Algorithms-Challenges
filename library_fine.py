# Function Description:
#     Complete the libraryFine function in the editor below.
#     libraryFine has the following parameter(s):
#         d1, m1, y1: returned date day, month and year, each an integer
#         d2, m2, y2: due date day, month and year, each an integer
#
# Returns:
#     int: the amount of the fine or 0 if there is none
#
# Input Format:
#     The first line contains 3 space-separated integers, d1, m1, y1, denoting the respective day, month, and year on
#     which the book was returned.
#     The second line contains 3 space-separated integers, d2, m2, y2, denoting the respective day, month, and year on
#     which the book was due to be returned.

import os


def libraryFine(d1, m1, y1, d2, m2, y2):
    count = 0
    if y1 == y2:
        if m1 == m2:
            if d1 <= d2:
                count += 0
            else:
                count += (15 * (d1 - d2))
        elif m1 < m2:
            count += 0
        else:
            count += (500 * (m1 - m2))
    elif y1 < y2:
        count += 0
    else:
        count += 10000
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    d1 = int(first_multiple_input[0])

    m1 = int(first_multiple_input[1])

    y1 = int(first_multiple_input[2])

    second_multiple_input = input().rstrip().split()

    d2 = int(second_multiple_input[0])

    m2 = int(second_multiple_input[1])

    y2 = int(second_multiple_input[2])

    result = libraryFine(d1, m1, y1, d2, m2, y2)

    fptr.write(str(result) + '\n')

    fptr.close()
