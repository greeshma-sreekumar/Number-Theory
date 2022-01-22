# print catalan numbers in the given range
r = int(input("Enter the no.of terms: "))
def print_catalan_num(r):
    print([math.factorial(2*x)//((math.factorial(x)**2)*(x+1)) for x in range(r)])

print_catalan_num(r)
