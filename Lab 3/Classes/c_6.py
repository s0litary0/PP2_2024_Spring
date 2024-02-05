def isprime(x):
    k = 0
    for i in range(1, x + 1):
        if x % i == 0:
            k += 1
    if k == 2:
        return True
    else:
        return False

primes = filter(isprime, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(list(primes))