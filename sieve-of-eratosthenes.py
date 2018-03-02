from math import sqrt, floor

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


if __name__ == '__main__':
    print(sieve(20))
