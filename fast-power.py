# Computes base^exp (mod 'mod')
def fast_power(base, exp, mod):
    if exp == 0:
        x = 1
    else:
        half = fast_power(base, exp // 2, mod)
        x = half * half
        if exp % 2 == 1:
            x *= base
    return x % mod
