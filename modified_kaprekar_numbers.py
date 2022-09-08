# Function Description:
#     Complete the kaprekarNumbers function in the editor below.
#     kaprekarNumbers has the following parameter(s):
#         int p: the lower limit
#         int q: the upper limit
#
# Prints:
#     It should print the list of modified Kaprekar numbers, space-separated on one line and in ascending order.
#     If no modified Kaprekar numbers exist in the given range, print INVALID RANGE. No return value is required.
#
# Input Format:
#     The first line contains the lower integer limit `p`.
#     The second line contains the upper integer limit `q`.
#     Note: Your range should be inclusive of the limits.

def kaprekarNumbers(p, q):
    total = []
    for x in range(p, q + 1):
        squ = x * x
        first = squ // 10 ** len(str(x))
        last = squ % 10 ** len(str(x))
        if first + last == x:
            total.append(x)
    if len(total) == 0:
        print("INVALID RANGE")
    else:
        print(*total)


if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
