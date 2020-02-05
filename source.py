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
    i = 0

    while len(my_prime_list) != 10 and i < 1000:
        value = random.randint(10000, 20000)
        if test_prime_brute_force(value):
            my_prime_list.append(value)
        i += 1

    return my_prime_list


def calc_n_fn(p, q):
    n = p * q
    fn = (p-1) * (q-1)

    return n, fn


def extended_gcd(a=1,b=1):
    if a < b:
        a, b = b, a
        print('Switched two arguments to ensure a >= b.')
    if b == 0:
        return 1, 0, a
    (x, y, d) = extended_gcd(b, a % b)
    return y, x - a//b*y, d


def generate_keys():
    
    # Public key
    primes = generating_prime_numbers()
    while True:
        p = primes[random.randint(0, len(primes) - 1)]
        q = primes[random.randint(0, len(primes) - 1)]
        if math.gcd(p, q) == 1:
            break
    n, fn = calc_n_fn(p, q)

    while True:
        e = random.randint(2, fn)
        if math.gcd(fn, e) == 1:
            break
    # Private key
    (x, y, d) = extended_gcd(fn, e)
    if y < 0:
        y += fn
    return n, e, y


def encrypt_message(message='Hello', e=5, n=119):
    encrypted = []
    for i in range(0, len(message)):
        a = ord(message[i])
        c = pow(a, e, n)
        encrypted.append(c)

    return encrypted


def decrypt_message(encrypted=[4, 33, 75, 75, 76], d=77, n=119):
    decrypted = []
    for i in range(0, len(encrypted)):
        a = encrypted[i]
        m = pow(a, d, n)
        decrypted.append(chr(m))

    return decrypted


def main_menu():
    print('Welcome to the RSA encryption and decryption service.\n')

    while True:
        menu_input = input('Input(m) for Message or Input(d) for Digital Signature: ').upper()
        if menu_input == 'M':
            message_menu()
        elif menu_input == 'D':
            digital_signature_menu()
        else:
            print('You have enter the wrong input')

        if menu_input == 'M' or menu_input == 'D':
            break


def message_menu():
    print('message menu')
    while True:
        menu_input = input('Select (1) for Encryption,(2) for Decryption, or (3) to Close')
        n, e, y = generate_keys()
        if menu_input == 1:
            message = input('Message to encrypt: ')            
            eMessage = encrypt_message(message, e, n)
            print('Encrypted message: ' + eMessage)
        elif menu_input == 2:
            eMessage = input('Encrypted message: ')
            message = decrypt_message(eMessage,y,n)
            print('Decrypted message: ' + message)
        elif menu_input == 3:
            break
        else:
            print('Invalid input. Try again.')

def digital_signature_menu():
    print('Digital signature menu')
    while True:
        menu_input = input('Select (1) to Sign, (2) to Verify, or (3) to Close')
        n, e, y = generate_keys()
        if menu_input == 1:
            signature = input('Signature: ')            
            eSignature = encrypt_message(signature, e, n)
            print('Encrypted signature: ' + eSignature)
        elif menu_input == 2:
            eSignature = input('Encrypted signature to verify: ')
            signature = decrypt_message(eSignature,y,n)
            print('Decrypted signature: ' + signature)
        elif menu_input == 3:
            break
        else:
            print('Invalid input. Try again.')

def main():
    n, e, d = generate_keys()
    encrypted = encrypt_message(message='MyNameIsLongtin', e=e, n=n)
    print(encrypted)
    print(decrypt_message(encrypted=encrypted, d=d, n=n))
    main_menu()


main()
