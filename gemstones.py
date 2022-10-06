# Function Description:
#     Complete the gemstones function in the editor below.
#     gemstones has the following parameter(s):
#         string arr[n]: an array of strings
#
# Returns:
#     int: the number of gemstones found
#
# Input Format:
#     The first line consists of an integer `n`, the size of arr.
#     Each of the next `n` lines contains a string arr[i] where each letter represents an occurence of a mineral in
#     the current rock.

import os


def gemstones(arr):
    count = set(arr[0])
    for a in arr[1::]:
        count = count.intersection(set(a))
    return len(count)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
