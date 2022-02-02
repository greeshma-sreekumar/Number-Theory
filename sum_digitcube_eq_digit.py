# print digits are equal to sum of cube of its digits

def sum_eq_digitcube_number(n, m):
    for i in range(n, m):
        a = str(i)
        b = [int(x)**3 for x in a]
        if sum(b) == i:
            print(i, end=" ")

sum_eq_digit_number(100,1000)
