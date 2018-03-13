from random import randint


# returns true if n is (probably) prime, false if composite
def miller_rabin(n):
    if n < 2:
        return False
    m, q = remove_twos(n-1, 0)
    for i in range(100):
        composite = True
        rand_b = randint(1, n-1)  # choosing a witness
        x = pow(rand_b, m, n)
        if x == 1 or x == n-1:
            composite = False
        for j in range(1, q):
            x = (x**2) % n
            if x == n-1:
                composite = False
        if composite:
            return False
    return True


# returns odd integer m such that n=(2^q)m for some q, returns m and q
def remove_twos(n, q):
    if n % 2 != 0:
        return n, q
    else:
        return remove_twos(n // 2, q + 1)


if __name__ == '__main__':
    while True:
        print()
        try:
            n = int(input("Enter a number: "))
        except:
            break
        composite = miller_rabin(n)
        if composite:
            print('composite')
        else:
            print('probably prime')

    '''
    primes = []
    x = 2
    while True:
        if not is_composite(x):
            primes.append(x)
            print(x)
        x += 1
    print(primes)'''
