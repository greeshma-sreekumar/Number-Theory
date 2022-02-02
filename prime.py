#check if prime
def check_prime(n):
    for i in range(2, int(n**0.5)):
        if n%i==0:return "NO"
        else:return "YES"

print(check_prime(263))
