
def sieve(n):
    m = [i for i in range(2, n+1)]
    print(m)
    for j in range(2, n+1):
        m[j] = 0
    j = 2
    while j * j <= n:
        if m[j] == 0:
            i = j * j
            while i <= n:
                if m[i] == 0:
                    m[i] = j
                i = i + j
        j += 1
    return m

print(sieve(10))
