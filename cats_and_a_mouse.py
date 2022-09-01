# Function Description:
#     Complete the catAndMouse function in the editor below.
#     catAndMouse has the following parameter(s):
#         int x: Cat A's position
#     int y: Cat B's position
#     int z: Mouse C's position
#
# Returns:
#     string: Either 'Cat A', 'Cat B', or 'Mouse C'
#
# Input Format:
#     The first line contains a single integer, `q`, denoting the number of queries.
#     Each of the `q` subsequent lines contains three space-separated integers describing the respective values of
#     x(cat A's location), y(cat B's location), and z(mouse C's location).

import os


def catAndMouse(x, y, z):
    cat_a = abs(z - y)
    cat_b = abs(z - x)
    if cat_a > cat_b:
        return 'Cat A'
    elif cat_b > cat_a:
        return 'Cat B'
    else:
        return 'Mouse C'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
