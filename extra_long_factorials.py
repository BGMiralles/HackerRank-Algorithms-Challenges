# Function Description:
#     Complete the extraLongFactorials function in the editor below. It should print the result and return.
#     extraLongFactorials has the following parameter(s):
#         n: an integer
#
# Input Format:
#     Input consists of a single integer `n`.


def extraLongFactorials(n):
    x = 1
    while n > 0:
        x *= n
        n -= 1
    return print(x)


if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)
