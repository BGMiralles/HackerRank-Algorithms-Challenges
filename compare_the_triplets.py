# Example:
#     a = [1, 2, 3]
#     b = [3, 2, 1]
#         For elements *0*, Bob is awarded a point because a[0] .
#         For the equal elements a[1] and b[1], no points are earned.
#         Finally, for elements 2, a[2] > b[2] so Alice receives a point.
#
#     The return array is [1, 1] with Alice's score first and Bob's second.
#
# Function Description:
#     Complete the function compareTriplets in the editor below.
#     compareTriplets has the following parameter(s):
#         int a[3]: Alice's challenge rating
#         int b[3]: Bob's challenge rating
#
# Return:
#     int[2]: Alice's score is in the first position, and Bob's score is in the second.
#
# Input Format:
#     The first line contains 3 space-separated integers, a[0], a[1], and a[2], the respective values in triplet a.
#     The second line contains 3 space-separated integers, b[0], b[1], and b[2], the respective values in triplet b.

import os

def compareTriplets(a, b):
    alice, bob = 0, 0
    for x, y in zip(a, b):
        alice += x > y
        bob += x < y
    result = [alice, bob]
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
