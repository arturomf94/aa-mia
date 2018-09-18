count = 0

def prime(n):
    global count

    if n <= 1:
        return False
    count += 1
    if n == 2:
        return True 
    count += 1  
    if n % 2 == 0:
        return False
    count += 1
    d = 3
    while d * d <= n:
        if (n % d == 0):
            return False
        count += 1
        d += 2 
    return True

def count_primes(n):
    global count
    primes = 0
    i = 1
    while(i <= n):
        count += 1
        if prime(i):
            primes += 1
        i += 1
    return primes

import pdb; pdb.set_trace()