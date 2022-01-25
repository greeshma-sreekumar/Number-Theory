# finding digital root

num = int(input("Enter an intiger: "))
def digital_root(num):
    if num%9==0:return 9
    else:return num%9

print(digital_root(num))

# checking if a number is square or not using digital root
n = int(input("Enter the number to be checked: "))
def check_sqr(n):
    if digital_root(n) in [1, 4, 7, 9]: return "yes"
    else: return "no"

check_sqr(n)
