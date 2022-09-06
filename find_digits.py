# Function Description:
#     Complete the findDigits function in the editor below.
#     findDigits has the following parameter(s):
#         int n: the value to analyze
#
# Returns:
#     int: the number of digits in `n` that are divisors of `n`.
#
# Input Format:
#     The first line is an integer, `t`, the number of test cases.
#     The `t` subsequent lines each contain an integer, `n`.

import os


def findDigits(n):
    count = 0
    for x in str(n):
        if int(x) != 0 and n % int(x) == 0:
            count += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
