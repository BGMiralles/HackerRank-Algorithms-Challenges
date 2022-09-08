# Function Description:
#     Complete the serviceLane function in the editor below.
#     serviceLane has the following parameter(s):
#         int n: the size of the width array
#         int cases[t][2]: each element contains the starting and ending indices for a segment to consider, inclusive
#
# Returns:
#     int[t]: the maximum width vehicle that can pass through each segment of the service lane described
#
# Input Format:
#     The first line of input contains two integers, `n` and `t`, where `n` denotes the number of width measurements
#     and `t`, the number of test cases. The next line has `n` space-separated integers which represent the array width.
#     The next `t` lines contain two integers, `i` and `j`, where `i` is the start index and `j` is the end index of the
#     segment to check.

import os


def serviceLane(n, cases):
    ans = []
    for i in range(len(cases)):
        ans.append(min(width[cases[i][0]:(cases[i][1]+1)]))
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    width = list(map(int, input().rstrip().split()))

    cases = []

    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    result = serviceLane(n, cases)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
