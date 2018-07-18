from math import sqrt, floor
import numpy as np
from time import time

# Returns a tagged list of numbers 2..n with tag True if prime, False if not
def sieve(n):
    A = [True for i in range(n+1)]
    A[0] = A[1] = False
    for i in range(2, floor(sqrt(n))):
        if A[i] is True:
            j = i**2
            while j < len(A):
                A[j] = False
                j += i
    return A[2:]

def sieve2(n):
    A = np.ones(n, dtype=bool)
    A[:2] = False
    m = int(np.sqrt(n))
    for i in range(2, m):
        if A[i] == True:
            A[i*i::i] = False
    #return np.nonzero(A)[0]
    return A

# Returns a list of all primes less than or equal to n
def prime_list(n):
    A = sieve2(n)
    return np.nonzero(A)[0]


if __name__ == '__main__':
    print(len(prime_list(200)))
