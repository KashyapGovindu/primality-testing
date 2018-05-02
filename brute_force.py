from math import sqrt

def brute_force_prime_test(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    while True:
        print()
        try:
            n = int(input("Enter a number: "))
        except:
            break

        if brute_force_prime_test(n):
            print("PRIME")
        else:
            print("COMPOSITE")
