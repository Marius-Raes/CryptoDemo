from sympy import randprime, lcm
import json

def createKeys():
    p = q = 1
    # p and q cant be the same 
    while(p == q):
        p = randprime(2**64, 2**128)

        q = randprime(2**64, 2**128)

    # n is garanteed to be between 128 and 256 bits
    n = p*q

    # e with low hamming weight
    e = 2**16 + 1

    #create prvate key
    lcm(p-1, q-1)

    d = pow(e, -1, int(lcm(p-1, q-1)))

    keys = {"public": {"n": n, "e": e}, "private": {"n": n, "d": d}}

    return keys

#import random

#m = random.getrandbits(128)

#encrypted = m**e % n

#decrypted = pow(encrypted, d, n)

