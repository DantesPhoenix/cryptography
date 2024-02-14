import random
import math

#function checking if number is prime or not 
def is_prime(number):
    if number < 2:
        return False

    for i in range(2, number // 2 +1):
        if number % i == 0:
            return False
    
    return True  

#function to generate prime number 
def generate_prime(min_value, max_value):
    prime = random.randint(min_value, max_value)
    while not is_prime(prime):
        prime = random.randint(min_value, max_value)
    return prime

#function to generate private key
def mod_inverse(e, phi):
    for d in range(3, phi):
        if (d * e) % phi == 1:
            return d

    #display error message if key is not valid
    raise ValueError("mod_inverse does not exist")

#deining prime numbers in range
p, q = generate_prime(1000, 5000), generate_prime(1000, 5000)

#checking that primes are not the same
while p == q:
    q = generate_prime(1000, 5000)

#getting n (both primes timesed together)
n = p * q

# getting modulus of n
phi_n = (p - 1) * (q - 1)

#generating public key
e = random.randint(3, phi_n-1)
while math.gcd(e, phi_n) !=1:
    e = random.randint(3, phi_n-1)

#calling function for creation of private key
d = mod_inverse(e, phi_n)

#print keys, n, modulus of n, and both primes
print("Public Key: ", e)
print("Private Key: ", d)
print("n: ", n)
print("Phi of n: ", phi_n)
print("p: ", p)
print("q: ", q)

#getting message to be encrypted
message = input("please enter message to be encrypted: ")

#converting all characters in message to ASCII 
message_encoded = [ord(ch) for ch in message]

#getting encoded text with formula (m ^ e) mod n 
ciphertext = [pow(ch, e, n) for ch in message_encoded]

print(ciphertext)

#decoding message and adding it to a string 
message_decoded = [pow(ch, d, n) for ch in ciphertext]
decoded_message = "".join(chr(ch) for ch in message_decoded)

print(decoded_message)
