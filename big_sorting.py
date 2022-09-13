# Function Description:
#     Complete the bigSorting function in the editor below.
#     bigSorting has the following parameter(s):
#         string unsorted[n]: an unsorted array of integers as strings
#
# Returns:
#     string[n]: the array sorted in numerical order
#
# Input Format:
#     The first line contains an integer, `n`, the number of strings in unsorted.
#     Each of the `n` subsequent lines contains an integer string, unsorted[i].

import os


def bigSorting(unsorted):
    return sorted(unsorted, key=int)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
