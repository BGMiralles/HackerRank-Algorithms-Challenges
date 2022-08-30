# Function Description:
#     Complete the function kangaroo in the editor below.
#     kangaroo has the following parameter(s):
#         int x1, int v1: starting position and jump distance for kangaroo 1
#         int x2, int v2: starting position and jump distance for kangaroo 2
#
# Returns:
#     string: either YES or NO
#
# Input Format:
#     A single line of four space-separated integers denoting the respective values of x1, v1, x2, and v2.

def kangaroo(x1, v1, x2, v2):
    kang1 = x1
    kang2 = x2
    for x in range(1, 5):
        kang1 += v1
    for x in range(1, 5):
        kang2 += v2
    if kang1 == kang2:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)