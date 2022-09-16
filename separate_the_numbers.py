# Function Description:
#     Complete the separateNumbers function in the editor below.
#     separateNumbers has the following parameter:
#         s: an integer value represented as a string
#
# Prints:
#     - string: Print a string as described above. Return nothing.
#
# Input Format:
#     The first line contains an integer `q`, the number of strings to evaluate.
#     Each of the next `q` lines contains an integer string `s` to query.


def separateNumbers(s):
    n = len(s)
    for i in range(1,1+n//2):
        temp_int = int(s[:i])
        j=0
        temp_str = ""
        while(len(temp_str) < n):
            temp_str += str(temp_int + j)
            j += 1
        if temp_str == s:
            print("YES {}".format(temp_int))
            return
    print("NO")
    

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
