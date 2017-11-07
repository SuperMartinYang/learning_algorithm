def gcd(num1, num2):
    while num2 and num1:
        tmp = num1
        num1 = num2 % num1
        num2 = tmp
    return num2

def all_relative_prime(p,q):
    n = p*q
    for i in range(n):
        if gcd(i, (p-1)*(q-1)) == 1:
            print(i)

all_relative_prime(7,33)