# Function Description:
#     Complete the insertionSort2 function in the editor below.
#     insertionSort2 has the following parameter(s):
#         int n: the length of arr
#         int arr[n]: an array of integers
#
# Prints:
#     At each iteration, print the array as space-separated integers on its own line.
#
# Input Format:
#     The first line contains an integer, `n`, the size of arr.
#     The next line contains `n` space-separated integers arr[i].


def insertionSort2(n, arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while j >= 0 and temp < arr[j]:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = temp
        print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
