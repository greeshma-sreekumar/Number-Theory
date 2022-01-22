# print pascals triangle
n = int(input("Enter the rows needed: "))
def pascals_triangle(n):
    for i in range(1, n + 1):
        for j in range(0, n - i + 1):
            print(' ', end='')
        a = 1
        for j in range(1, i + 1):
            print(' ', a, sep='', end='')
            a = a * (i - j) // j
        print()


pascals_triangle(n)
