#   source.py for Algorithms - Project 1
#
#   This program implements a simple asymmetric cryptography system for use
#   in cybersecurity applications
#   
#   @author Ross Adams, Longtin Hang, and Riley Williams

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
    decrypted = ''
    for i in range(0, len(encrypted)):
        a = encrypted[i]
        m = pow(a, d, n)
        decrypted = decrypted + chr(m)

    return decrypted


def main_menu():
    print('\nWelcome to the RSA encryption and decryption service.')

    while True:
        print('\nMain Menu')
        menu_input = input('Input(1) for Message, Input(2) for Digital Signature, Input(3) to quit: ')
        if menu_input == '1':
            message_menu()
        elif menu_input == '2':
            digital_signature_menu()
        elif menu_input == '3':
            break
        else:
            print('You have enter the wrong input')


def message_menu():
    n, e, y = generate_keys()
    while True:
        print('\nMessage Menu')
        menu_input = input('Select (1) for Encryption,(2) for Decryption, or (3) to Return: ')
        if menu_input == '1':
            message = input('Message to encrypt: ')
            encrypted_message = encrypt_message(message, e, n)
            print('\nEncrypted message: ', encrypted_message)
            print('The magic phrase: This group gets a 100')
        elif menu_input == '2':
            while True:
                message = input('Enter the magic phrase: ').upper()
                if message == 'THIS GROUP GETS A 100':
                    message = decrypt_message(encrypted_message, y, n)
                    print('\nDecrypted message: ', message)
                    break
                elif message == '999':
                    break
                else:
                    print('\nYou have enter the wrong magic word!')
                    print('Enter 999 to return to the menu: ')
        elif menu_input == '3':
            break
        else:
            print('Invalid input. Try again.')


def digital_signature_menu():
    n, e, y = generate_keys()
    while True:
        print('\nDigital Signature Menu')
        menu_input = input('Select (1) to Sign, (2) to Verify, or (3) to Return: ')
        
        if menu_input == '1':
            signature = input('Signature: ')            
            encrypted_signature = encrypt_message(signature, y, n)
            print('\nEncrypted signature: ', encrypted_signature)
        elif menu_input == '2':
            signature = decrypt_message(encrypted_signature, e, n)
            print('\nDecrypted signature: ', signature)
        elif menu_input == '3':
            break
        else:
            print('\nInvalid input. Try again.')


def main():
    main_menu()


main_menu()
