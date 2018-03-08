from perfect_power import perfect_power
import numpy as np
from sieve_of_eratosthenes import sieve2
from math import sqrt
from scipy.special import binom

## DOES NOT WORK YET ##
# Returns True if n is a prime, False if n is composite
def aks(n):
    if n < 2:
        print("Invalid input.")
        return
    if perfect_power(n) == True:
        print(n, "determined composite in step 1")
        return False
    r = 2
    lim1 = int(4 * pow(np.ceil(np.log2(n)), 2))
    while r < n:
        if n % r == 0:
            print(n, "determined composite in step 2")
            return False
        limit = int(pow(2, np.ceil(np.log2(r))))
        is_prime = sieve2(limit + 1)
        if is_prime[r] == True:
            #print("here for", n)
            if subroutine(n, r, lim1) == True:
                break
        r += 1
    if r == n:
        print(n, "determined prime in step 3")
        return True
    lim2 = int(2 * np.ceil(sqrt(r)) * np.ceil(np.log2(n)))
    for a in range(1, lim2):
        coefficients = [binom(n, i) * pow(a, n-i) for i in range(n+1)]

        # modulus = X^r - 1
        modulus = [0 for i in range(len(coefficients))]
        modulus[r] = 1  # maybe modulus[r+1]?
        modulus[0] = -1
        
        # check = X^(n mod r) + a
        check = [0 for i in range(len(coefficients))]
        check[n % r] = 1
        check[0] = a
        result = np.polydiv(coefficients, modulus)[1]
        print(result)
        if not (check == result):
            print(n, "determined composite in step 4")
            return False
    print(n, "determined prime in step 5")
    return True
        # Test the polynomial equivalencies here
    
# Returns whether or not we should break from the while loop in aks
def subroutine(n, r, limit):
    #print(n, r, limit)
    for i in range(1, limit + 1):
        if pow(n, i, r) == 1:
            return False
    #print("returning true")
    return True

# Returns a list of the primes 2 <= p <= n to check with the AKS output
def list_primes(n):
    A = np.ones(n, dtype=bool)
    A[:2] = False
    m = int(np.sqrt(n))
    for i in range(2, m):
        if A[i] == True:
            A[i*i::i] = False
    return np.nonzero(A)[0]

if __name__=='__main__':
    #aks(5)
    for i in range(2, 500):
        aks(i)
    '''maybe_primes = []
    for i in range(2, 200):    
        if aks(i):
            maybe_primes.append(i)
    print(maybe_primes)
    print(list_primes(200))'''

