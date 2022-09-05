# Function Description:
#     Complete the angryProfessor function in the editor below. It must return YES if class is cancelled, or NO otherwise.
#     angryProfessor has the following parameter(s):
#         int k: the threshold number of students
#         int a[n]: the arrival times of the `n` students
#
# Returns:
#     string: either YES or NO
#
# Input Format:
#     The first line of input contains `t`, the number of test cases.
#     Each test case consists of two lines.
#     The first line has two space-separated integers, `n` and `k`, the number of students (size of `a`) and the
#     cancellation threshold.
#     The second line contains `n` space-separated integers (a[1], a[2], ..., a[n]) that describe the arrival times
#     for each student.

import os


def angryProfessor(k, a):
    count = 0
    for x in a:
        if x <= 0:
            count += 1
    if count >= k:
        return "NO"
    else:
        return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        fptr.write(result + '\n')

    fptr.close()
