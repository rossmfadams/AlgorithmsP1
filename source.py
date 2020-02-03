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

def extended_gcd(a=1,b=1):
    if a < b:
        a, b = b, a
        print('Switched two arguments to ensure a >= b.')
    if b == 0:
        return (1,0,a)
    (x,y,d) = extended_gcd(b,a%b)
    return y,x - a//b*y, d

def generate_keys():
    
    ## Public key
    primes = generating_prime_numbers()
    while True:
        p = primes[random.randint(0,len(primes))]
        q = primes[random.randint(0,len(primes))]
        if math.gcd(p,q) == 1:
            break
    n, fn = calc_n_fn(p,q)

    while True:
        e = random.randint(2,fn)
        if math.gcd(fn,e) == 1:
            break
    ## Private key
    (x,y,d) = extended_gcd(fn,e)
    if x < 0:
        x += fn
    return (n, e, x)

def encrypt_message(message = 'Hello', e = 5, n = 119):
    encrypted = []
    for i in range(0, len(message)):
        a = ord(message[i])
        c = pow(a, e, n)
        encrypted.append(c)

    return encrypted

def decrypt_message(encrypted = [4,33,75,75,76], d = 77, n = 119):
    decrypted = []
    for i in range(0, len(encrypted)):
        a = encrypted[i]
        m = pow(a, d, n)
        decrypted.append(chr(m))

    return decrypted
