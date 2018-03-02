from perfect_power import perfect_power
import numpy as np
from sieve_of_eratosthenes import sieve2
from math import sqrt
from scipy.special import binom

## DOES NOT WORK YET ##
# Returns True if n is a prime, False if n is composite
def aks(n):
    if perfect_power(n):
        return False
    r = 2
    lim1 = int(4 * pow(np.ceil(np.log2(n)), 2))
    while r < n:
        if n % r == 0:
            return False
        limit = int(pow(2, np.ceil(np.log2(r))))
        is_prime = sieve2(limit + 1)
        if is_prime[r] == True:
            if subroutine(n, r, lim1):
                break
        r += 1
    if r == n:
        return True
    lim2 = 2 * np.ceil(sqrt(r)) * np.ceil(np.log2(n))
    for a in range(1, lim2):
        coefficients = [binom(n, i) * pow(a, n-i) for i in range(n+1)]
    return "hello"
        # Test the polynomial equivalencies here
    
# Returns whether or not we should break from the while loop in aks
def subroutine(n, r, limit):
    for i in range(1, limit + 1):
        if pow(n, i, r) == 1:
            return False
    return True

if __name__=='__main__':
    for i in range(10):    
        print(i, aks(7))
