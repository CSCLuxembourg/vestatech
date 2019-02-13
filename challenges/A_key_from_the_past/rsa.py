#! /usr/bin/env python
#-*- coding: utf-8 -*-

import random

import utils

class RSA():
    def __init__(self, p=None, q=None, a=None, b = None, n=None, nb_bits=4096):
        """Initializes the magic keys.
        """
        if p is None and q is None and a is None:
            # 1. Generates 'p' and 'q' prime numbers of lengths 'nb_bits' in a 
            # random fashion.
            if p is None and q is None: 
                p = random.getrandbits(nb_bits)
                q = random.getrandbits(nb_bits)
                while not utils.miller_rabin(p):
                    p = random.getrandbits(nb_bits)
                while not utils.miller_rabin(q):
                    q = random.getrandbits(nb_bits)

        if a is None and b is None and n is None:
            # 2. Generates 'a', 'b' and 'n' thanks to 'phi' and 'b'.
            n   = p * q
            phi = (p - 1) * (q - 1)
            if b is None:
                while True:
                    b = random.randint(2, phi - 1)
                    if utils.is_prime_together(b, phi):
                        break
            a  = utils.inv_modulo(b, phi)

        self.private = a
        self.public = b
        self.modulus = n


    def encrypt_int(self, x):
        """Encrypt an integer."""
        return pow(x, self.public, self.modulus)

    def decrypt_int(self, y):
        """Decrypt an integer."""
        raise Exception("Hey not too fast! First solve this challenge: https://github.com/cscluxembourg/vestatech/tree/master/challenges/Sergei_forgot_his_formula")


    def __str__(self):
        """Pretty print of the keys."""
        return """\
            Private key: %s
            Public key: %s
            Modulus: %s
            """ % (self.private, self.public, self.modulus)
