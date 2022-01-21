# print polygonal numbers
p = int(input("Enter the no.of edges of the polygon: "))
n = int(input("Enter no.of terms needed: "))
def printPoluNum(p,n):
    for i in range(1, n):
        m = ((p-2)*i*(i+1)/2) -((p-3)*i)
        print(int(m), end=" ")


printPoluNum(p,n)

#find if a number is 
