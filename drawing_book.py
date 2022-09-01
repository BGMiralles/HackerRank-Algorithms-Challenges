Function Description

Complete the pageCount function in the editor below.

pageCount has the following parameter(s):

    int n: the number of pages in the book
    int p: the page number to turn to

Returns

    int: the minimum number of pages to turn

Input Format

The first line contains an integer
, the number of pages in the book.
The second line contains an integer, , the page to turn to.

def pageCount(n, p):
    begin = int(p // 2)
    if (n % 2 == 0) and (n - p == 1):
        end = 1
    else:
        end = int((n // 2 - p // 2))
    return min(begin, end)

if __name__ == '__main__':

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

print(result)
