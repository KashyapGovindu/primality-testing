from random import randint
from math import gcd
from brute_force import brute_force_prime_test

PRIME = True
COMPOSITE = False

THRESHOLD = 40   # Number of times Miller-Rabin should run

# INPUT: Integer n to be tested, integer a as potential witness
# returns true if n is (probably) prime, false if composite
def miller_rabin(n):
    if n < 2:
        print("Primality not defined for numbers < 2")
        return None
    if n == 2:
        return PRIME


    for i in range(THRESHOLD):
        possibly_prime = False
        a = randint(1, n-1)
        if n < 2 or n % 2 == 0 or gcd(a, n) > 1:
            return COMPOSITE
        q, k = remove_twos(n-1, 0)
        #print(q, k)
        a = pow(a, q, n)
        if a == 1:
            possibly_prime = True #return PRIME
            continue
        for i in range(k):
            #print("a=", a)
            if a == n - 1:
                possibly_prime = True
                break #return PRIME
            a = pow(a, 2, n)
        if possibly_prime:
            continue
        else:
            return COMPOSITE
    return PRIME


# returns odd integer m such that n=(2^k)q for odd q, returns q and k
def remove_twos(n, k):
    if n % 2 != 0:
        return n, k
    else:
        return remove_twos(n // 2, k + 1)


def testing():
    passed = True
    for i in range(2, 1000):
        #rand_a = randint(1, i-1)
        if miller_rabin(i) != brute_force_prime_test(i):
            passed = False
            print(i, miller_rabin(i), brute_force_prime_test(i))
    if passed:
        print("success")

if __name__ == '__main__':
    testing()
    while True:
        print()
        try:
            n = int(input("Enter a number: "))
        except:
            break

        result = miller_rabin(n)
        if result == COMPOSITE:
            print('COMPOSITE')
        elif result == PRIME:
            print('PRIME')

    '''
    primes = []
    x = 2
    while True:
        if not is_composite(x):
            primes.append(x)
            print(x)
        x += 1
    print(primes)'''
