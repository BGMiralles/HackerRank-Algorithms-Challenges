# Function Description:
#     Complete the workbook function in the editor below.
#     workbook has the following parameter(s):
#         int n: the number of chapters
#         int k: the maximum number of problems per page
#         int arr[n]: the number of problems in each chapter
#
# Returns:
#     - int: the number of special problems in the workbook
#
# Input Format:
#     The first line contains two integers `n` and `k`, the number of chapters and the maximum number of problems
#     per page.
#     The second line contains `n` space-separated integers arr[i] where arr[i] denotes the number of problems
#     in the `i` chapter.

import os


def workbook(n, k, arr):
    page = 1
    count = 0
    for i in arr:
        x = 1
        while x <= i:
            if page == x:
                count += 1
            if x % k == 0 and x != i:
                page += 1
            x += 1
        page += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
