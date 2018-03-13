from miller_rabin import miller_rabin
from fractions import gcd
import random


# Extended Euclidean Algorithm
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


# Returns multiplicative inverse of a mod m (d such that a * d = 1 (mod m))
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def random_prime(bits):
    probably_prime = False
    while not probably_prime:
        lower = pow(2, bits - 2)
        upper = pow(2, bits + 2)
        rand_p = random.randint(lower, upper)
        probably_prime = miller_rabin(rand_p)
    return rand_p


# Generates a public key N=pq with given number of bits, public encryption exponent e with gcd(e, (p-1)(q-1)) = 1
def generate_key(bits):
    e = 65537

    relatively_prime = False
    while not relatively_prime:
        p = random_prime(bits // 2)
        q = random_prime(bits // 2)
        if gcd(e, (p-1)*(q-1)) == 1:
            relatively_prime = True
    
    N = p*q

    return N, e, p, q


# Encrypt message given public key (N, e)
def encrypt(message, N, e):
    ciphertext = pow(message, e, N)  # c = m^e mod N
    return ciphertext


# Decrypt cipertext given public key (N, e), private key (p, q)
def decrypt(ciphertext, N, e, p, q):
    d = modinv(e, (p-1)*(q-1))
    message = pow(ciphertext, d, N)
    return message


# RSA with keys of bits length
def RSA(bits):
    print("Generating keys...")
    print()
    N, e, p, q = generate_key(bits)
    print("Public key: N = " + str(N) + " , e = " + str(e))
    print()
    plaintext = int(input("Enter plaintext between 0 and N: "))
    ciphertext = encrypt(plaintext, N, e)
    print()
    print("Encrypted message:", ciphertext)
    print()
    message = decrypt(ciphertext, N, e, p, q)
    print("Your message was:", message)


if __name__ == '__main__':
    #print(generate_public_key(1024))
    RSA(2048)