# Function Description:
#     Complete the insertionSort1 function in the editor below.
#     insertionSort1 has the following parameter(s):
#         n: an integer, the size of arr
#         arr: an array of integers to sort
#
# Returns:
#     None: Print the interim and final arrays, each on a new line. No return value is expected.
#
# Input Format:
#     The first line contains the integer `n`, the size of the array arr.
#     The next line contains `n` space-separated integers arr[0]...arr[n -1].


def insertionSort1(n, arr):
    for i in range(1, n):
        temp = arr[i]
        j = i
        while j > 0 and arr[j-1] > temp:
            arr[j] = arr[j-1]
            j = j - 1
            print(*arr)
        arr[j] = temp
    print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
