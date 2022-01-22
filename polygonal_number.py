# print polygonal numbers
p = int(input("Enter the no.of edges of the polygon: "))
n = int(input("Enter no.of terms needed: "))
def printPoluNum(p,n):
    for i in range(1, n):
        m = ((p-2)*i*(i+1)/2) -((p-3)*i)
        print(int(m), end=" ")


printPoluNum(p,n)

#find if a number is polygonal number
a = int(input("Enter the number to be checked: "))
def checkPolyNum(a,p):
    f = 0
    for i in range(1, 10**len(str(a))):
        m = ((p - 2) * i * (i + 1) / 2) - ((p - 3) * i)
        if a==m: f = i
    if f!=0: print("It is the "+str(f)+"th polygonal number")
    else:  print("It is not a polygonal number")
        
        
checkPolyNum(a, p)
