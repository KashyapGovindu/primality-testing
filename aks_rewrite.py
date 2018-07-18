from perfect_power import perfect_power
import numpy as np
from numpy.polynomial import polynomial as P
from sieve_of_eratosthenes import sieve2
from math import sqrt, ceil, gcd
from scipy.special import binom
from brute_force import brute_force_prime_test

PRIME = True
COMPOSITE = False

# Returns True if n is a prime, False if n is composite
def aks(n):
    if n < 2:
        print("Primality not defined for integers < 2")
        return

    if perfect_power(n):    # Step 1
        print(n, "determined COMPOSITE in Step 1")
        return COMPOSITE

    r = find_r(n)           # Step 2

    for a in range(2, r+1): # Step 3
        x = gcd(a, n)
        if 1 < x and x < n:
            print(n, "determined COMPOSITE in Step 3")
            return COMPOSITE

    if n <= r:              # Step 4
        print(n, "determined PRIME in Step 4")
        return PRIME

    # Step 5
    # ** Note that r-1 is an overestimate for phi(r) **
    limit = int(np.ceil(sqrt(r-1) * np.log2(n)))
    for a in range(1, limit):
        base = [a, 1]
        coefficients = fast_power_poly(base, n, r, n)
        check = np.zeros(len(coefficients))
        check[n % r] = 1
        check[0] = a
        if not (check == coefficients).all():
            print(n, "determined COMPOSITE in Step 5")
            return COMPOSITE

    print(n, "determined PRIME in Step 6")
    return PRIME             # Step 6



# Find the smallest r such that ord_r(n) not <= log^2 n
def find_r(n):
    limit = int(np.ceil((np.log2(n)) ** 2))

    r = 2
    while 1:
        found = True
        for k in range(1, limit):
            if n % r == 1:
                found = False
                break
        if found:
            return r
        r += 1


# base is array of coefficients, polynomial rings in Z_n
def fast_power_poly(base, power, r, Z_n):
    result = 1
    while power > 0:
        # If power is even
        if power % 2 == 0:
            # Divide the power by 2
            power = power / 2
            # Multiply base to itself
            base = P.polymul(base, base)
            #base = P.polydiv(square, modulus)[1]
            # base = base mod (x^r-1)
            x = np.nonzero(result)[0]
            for i in x[x>=r]:
                if base[i] != 0:
                    base[i % r] += base[i]
                    base[i] = 0
            # Keep the coefficients in Z_n
            base = base % Z_n
        else:
            # Decrement the power by 1 and make it even
            power = power - 1
            # Take care of the extra value that we took out
            # We will store it directly in result
            result = P.polymul(result, base)
            #result = P.polydiv(mult, modulus)[1]
            #print(np.nonzero(result))
            x = np.nonzero(result)[0]
            for i in x[x>=r]:
                #print(i)
                if result[i] != 0:
                    result[i % r] += result[i]
                    result[i] = 0
            # Keep the coefficients in Z_n
            result = result % Z_n

            # Now power is even, so we can follow our previous procedure
            power = power / 2
            base = P.polymul(base, base)
            #base = P.polydiv(square, modulus)[1]
            x = np.nonzero(result)[0]
            for i in x[x>=r]:
                if base[i] != 0:
                    base[i % r] += base[i]
                    base[i] = 0
            # Keep the coefficients in Z_n
            base = base % Z_n

    return result


def testing():
    primes_aks = []
    primes = []
    for i in range(2, 5000):
        if aks(i): primes_aks.append(i)
        if brute_force_prime_test(i): primes.append(i)

    if primes_aks == primes:
        print("success")
    else:
        print("failed")


if __name__=='__main__':
    '''base = [2, 12, 6, 1]
    power = 1
    r = 2
    n = 11
    print(fast_power_poly(base, power, r, n))
    #aks(5000011)'''


    while True:
        print()
        try:
            n = int(input("Enter a number: "))
        except:
            break

        result = aks(n)
        if result == COMPOSITE:
            print('COMPOSITE')
        elif result == PRIME:
            print('PRIME')
    '''maybe_primes = []
    for i in range(2, 200):
        if aks(i):
            maybe_primes.append(i)
    print(maybe_primes)
    print(list_primes(200))'''
