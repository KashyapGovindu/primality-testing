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

if __name__ == '__main__':
    t0 = time()
    sieve(1000000)
    t1 = time()
    sieve2(1000000)
    t2 = time()
    print("Sieve 1:", str(t1 - t0), "seconds")
    print("Sieve 2:", str(t2 - t1), "seconds")
