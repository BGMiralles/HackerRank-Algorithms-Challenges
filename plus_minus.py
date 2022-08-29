# Function Description:
#     Complete the plusMinus function in the editor below.
#     plusMinus has the following parameter(s):
#         int arr[n]: an array of integers
#
# Print:
#     Print the ratios of positive, negative and zero values in the array. Each value should be printed on a separate line
#     with 6 digits after the decimal. The function should not return a value.
#
# Input Format:
#     The first line contains an integer, `n`, the size of the array.
#     The second line contains space-separated integers that describe .
#
# Output Format:
#     Print the following 3 lines, each to 6 decimals:
#         proportion of positive values
#         proportion of negative values
#         proportion of zeros


def plusMinus(arr):
    postives = 0
    negative = 0
    zeros = 0
    for i in arr:
        if i > 0:
            postives += 1
        if i < 0:
            negative += 1
        if i == 0:
            zeros += 1

    print('{:.6f}'.format(postives / n))
    print('{:.6f}'.format(negative / n))
    print('{:.6f}'.format(zeros / n))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
