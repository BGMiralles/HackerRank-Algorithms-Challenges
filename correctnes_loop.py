# Challenge:
#     In the InsertionSort code below, there is an error. Can you fix it? Print the array only once,
#     when it is fully sorted.
#
# Input Format:
#     There will be two lines of input:
#     `s` - the size of the array
#     arr - the list of numbers that makes up the array

# def insertion_sort(l):
#     for i in range(1, len(l)):
#         j = i-1
#         key = l[i]
#         while (j > 0) and (l[j] > key):
#            l[j+1] = l[j]
#            j -= 1
#         l[j+1] = key
#
# m = int(input().strip())
# ar = [int(i) for i in input().strip().split()]
# insertion_sort(ar)
# print(" ".join(map(str,ar)))

def insertion_sort(l):
    for i in range(1, len(l)):
        j = i - 1
        key = l[i]
        while (j >= 0) and (l[j] > key):
           l[j+1] = l[j]
           j -= 1
        l[j+1] = key

m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
insertion_sort(ar)
print(" ".join(map(str,ar)))