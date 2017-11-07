def prime(x):
    if x == 2:
        return True
    else:
        for i in range(2,int(pow(x,0.5))):
            if x % i == 0:
                return False
        return True

print(prime(23))