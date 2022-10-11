# Formato de Entrada:
#     La primera linea contiene un enter `T` que quiere decir el número de casos de prueba. Luego siguen `T` lineas ,
#     con una cadena en cada linea.
#
# Formato de Salida:
#     Imprimie la mínima cantidad requerida de pasos en cada caso de prueba.

import os


def alternatingCharacters(s):
    count = 0
    for x, y in enumerate(s[1:]):
        if y == s[x]:
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
