from perfect-power import perfect_power

# Returns True if n is a prime, False if n is composite
def aks(n):
    if perfect_power(n):
        return False
    r = 2
    while r < n:
        if n % r == 0:
            return False
        if 
