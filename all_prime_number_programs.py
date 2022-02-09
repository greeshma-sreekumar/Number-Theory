#check if prime
def check_prime(n):
    for i in range(2, int(n**0.5)):
        if n%i==0:return "NO"
        else:return "YES"

print(check_prime(263))

# printprime in a given range
def primes(l,u):
    primes=[]
    for x in range(l, u+1):
        if x > 1:
            for i in range(2, x):
                if (x % i) == 0:break
            else: primes.append(x)
    return primes


print(primes(1, 100))

# list of twin primes from zero to a range
def twin_prime(n):
    prime=primes(0, n)
    for x in prime:
        for y in prime[1:]:
            if (y - x) == 2:
                print("(", x, y, ")", end=" ")

twin_prime(100)

# all palindromic primes from zero to a range
def palindrome_prime(n):
    prime = primes(0, n)
    for x in prime:
        if(str(x)==str(x)[::-1]):
            print(x, end=" ")

palindrome_prime(1000)

