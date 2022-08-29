# Function Description:
#     Complete the aVeryBigSum function in the editor below. It must return the sum of all array elements.
#     aVeryBigSum has the following parameter(s):
#         int ar[n]: an array of integers .
#
# Return:
#     long: the sum of all array elements
#
# Input Format:
#     The first line of the input consists of an integer `n`.
#     The next line contains `n` space-separated integers contained in the array.
#
# Output Format:
#     Return the integer sum of the elements in the array.


def aVeryBigSum(ar):
    return sum(ar)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
