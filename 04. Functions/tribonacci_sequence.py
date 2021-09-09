def printTribRec(n):
    if (n == 0 or n == 1 or n == 2):
        return 0

    elif (n == 3):
        return 1

    else:
        return (printTribRec(n - 1) +
                printTribRec(n - 2) +
                printTribRec(n - 3))


def printTrib(n):
    for i in range(1, n+3):

        if (i == 1 or i == 2):
            pass
        else:
            print(printTribRec(i), end=" ")


# Driver code
n = int(input())
printTrib(n)