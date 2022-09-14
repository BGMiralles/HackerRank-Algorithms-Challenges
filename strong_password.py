# Function Description:
#     Complete the minimumNumber function in the editor below.
#     minimumNumber has the following parameters:
#         int n: the length of the password
#         string password: the password to test
#
# Returns:
#     int: the minimum number of characters to add
#
# Input Format:
#     The first line contains an integer `n`, the length of the password.
#     The second line contains the password string. Each character is either a lowercase/uppercase English alphabet,
#     a digit, or a special character.

import os


def minimumNumber(n, password):
    number_count = 0
    lower_count = 0
    upper_count = 0
    special_count = 0
    min_len = 6 - n

    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for x in password:
        if x.isdigit():
            number_count += 1
        elif x in lower_case:
            lower_count += 1
        elif x in upper_case:
            upper_count += 1
        else:
            special_count += 1
        add = 0
        if number_count == 0:
            add += 1
        if lower_count == 0:
            add += 1
        if upper_count == 0:
            add += 1
        if special_count == 0:
            add += 1
    return max(add, min_len)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
