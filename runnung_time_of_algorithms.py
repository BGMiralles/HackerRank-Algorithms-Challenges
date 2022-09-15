# Function Description:
#     Complete the runningTime function in the editor below.
#     runningTime has the following parameter(s):
#         int arr[n]: an array of integers
#
# Returns:
#     int: the number of shifts it will take to sort the array
#
# Input Format:
#     The first line contains the integer `n`, the number of elements to be sorted.
#     The next line contains `n` integers of arr[arr[0]...arr[n - 1]].

import os


def runningTime(arr):
    count = 0
    for i in range(1, len(arr)):
        while arr[i] < arr[i-1] and i > 0:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            count += 1
            i = i - 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
