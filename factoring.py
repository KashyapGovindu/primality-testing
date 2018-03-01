from fractions import gcd

def pollard_factor(n):
    a = 2
    factor = None
    for i in range(2, 100):
        print("Set a=" + str(a) + "^" + str(i) + " = " + str(pow(a, i, n)) + " = 2^(" + str(i) + "!)")
        a = pow(a, i, n)
        g = gcd(a - 1, n)
        print("  gcd(" + str(a-1) + ", " + str(n) + ") = " + str(g))
        if g != 1:
            factor = g
            break
    return factor

n = 48356747
print(n, "has factor", pollard_factor(n))
