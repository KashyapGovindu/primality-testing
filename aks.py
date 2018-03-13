from perfect_power import perfect_power
import numpy as np
from numpy.polynomial import polynomial as P
from sieve_of_eratosthenes import sieve2
from math import sqrt
from scipy.special import binom


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
        base = [a, 1]  # Base = a+1*X = X+a
        modulus = np.zeros(r+1)
        #modulus = [0 for i in range(r+1)]
        modulus[0] = -1
        modulus[r] = 1  # modulus = X^r-1
        # Compute (X+a)^n
        coefficients = fast_power_poly(base, n, r, n)
        
        # check = X^(n mod r) + a
        #check = [0 for i in range(len(coefficients))]
        check = np.zeros(len(coefficients))
        check[n % r] = 1
        check[0] = a  # check = X^(n mod r) + a
        #print(check)
        #print(coefficients)
        if not (check == coefficients).all():
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

# brute force primality test to check our results
def brute_force_prime_test(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True



if __name__=='__main__':
    base = [2, 12, 6, 1]
    power = 1
    r = 2
    n = 11
    print(fast_power_poly(base, power, r, n))
    #aks(5000011)
    
    primes_aks = []
    primes = []
    for i in range(2, 500):
        if aks(i): primes_aks.append(i)
        if brute_force_prime_test(i): primes.append(i)

    if primes_aks == primes:
        print("success")
    else:
        print("failed")
    '''maybe_primes = []
    for i in range(2, 200):    
        if aks(i):
            maybe_primes.append(i)
    print(maybe_primes)
    print(list_primes(200))'''

