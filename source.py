# Place your code here
import math
import random


def test_prime_brute_force(p=10):
    if p == 2:
        return True
    else:
        for b in range(2, math.floor(math.sqrt(p))):
            if math.gcd(p, b) > 1:
                return False
            else:
                continue
        return True


def generating_prime_numbers():
    my_prime_list = []

    for i in range(100):
        value = random.randint(10000, 20000)
        if test_prime_brute_force(value):
            my_prime_list.append(value)

    return my_prime_list

def calc_n_fn(p, q):
    n = p * q
    fn = (p-1) * (q-1)

    return n, fn


def main():
    prime = generating_prime_numbers()
    print(prime)
    p = prime[0]
    q = prime[1]
    n, fn = calc_n_fn(p, q)
    print('n = ', n, ' fn = ', fn)


main()
