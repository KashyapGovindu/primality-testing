
# Checks if n >= 1 is a perfect power (n = a^b for some a, b >= 2)
def perfect_power(n):
    b = 2
    while pow(2, b) <= n:
        a = 1
        c = n
        while c-a >= 2:
            m = (a + c) // 2
            p = min(pow(m, b), n+1)
            if p == n:
                return True  # , m, b
            if p < n:
                a = m
            else:
                c = m
        b += 1
    return False

if __name__ == '__main__':
    while True:
        print()
        try:
            n = int(input("Enter a number: "))
        except:
            break
        pp = perfect_power(n)
        if pp:
            print('perfect power: ' + str(n) + '=' + str(pp[1]) + '^' + str(pp[2]))
        else:
            print('not a perfect power')
