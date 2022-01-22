# Print the square triangular numbers in the given range

print("Enter the range below")
b = int(input("Enter the range starting: "))
e = int(input("Enter the range ending: "))

def print_sqr_tri_num(b,e):
    for i in range(b, e):
        for j in range(b, e):
            if ((i*(i+1)/2) == j*j) and (len(str(j**2)) in range(len(str(e)))):
                print(j**2)

print_sqr_tri_num(b, e)
