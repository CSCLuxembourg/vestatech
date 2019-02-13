#! /usr/bin/env python
#-*- coding: utf-8 -*-

import random

from typing import List
 
 
 
def factors_decomposition(n: int) -> List[int]:
    raise Exception('Implement this or use whatever you want to do the job.')



def gcd(x,y):
    """Returns the gcd of x and y."""
    while y:
        (x, y) = (y, x%y)
    return abs(x)


def gcd_bezout(a,b):
    """Returns (d,u,v) such as d == gcd(a,b) == au + bv.
    """
    r0 = a
    r1 = b
    u0 = 0
    u1 = 1
    v0 = 1
    v1 = -r0//r1
    s = [r1,u0,v0]
    while r0 % r1:
        r = r0
        r0 = r1
        r1 = r%r1
        u = u0
        v = v0
        u0 = u1
        v0 = v1
        q = r0 // r1
        u1 = u-q*u1
        v1 = v-q*v1
        s = [r1, u0, v0]
    return s


def inv_modulo(a,m):
    """Returns the modular inverse of a modulo m.
    """
    (d, x, _) = gcd_bezout(a, m)
    if d == 1:
        return x % m
    return None


def is_prime_together(a, b):
    """Returns True if a and b are prime together.
    """
    return gcd(a, b) == 1


def miller_rabin_pass(a, s, d, n):
    """Miller Rabin primality test."""
    a_to_power = pow(a, d, n)
    if a_to_power == 1:
        return True
    for i in range(s-1):
        if a_to_power == n - 1:
            return True
        a_to_power = (a_to_power * a_to_power) % n
    return a_to_power == n - 1


def miller_rabin(n):
    """Primality test using Miller-Rabin method.
    n The number to test primality.
    """
    d = n - 1
    s = 0
    while d % 2 == 0:
        d >>= 1
        s += 1

    for repeat in range(20):
        a = 0
        while a == 0:
            a = random.randrange(n)
        if not miller_rabin_pass(a, s, d, n):
            return False
    return True
