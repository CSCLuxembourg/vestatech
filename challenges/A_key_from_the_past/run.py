#! /usr/bin/python
#-*- coding: utf-8 -*-

"""Execute this file to work on this challenge.
"""

import rsa
import utils

import time

if __name__ == '__main__':
    print("Factoring RSA modulus with weak prime factors\n")
    print("Loading RSA keys")
    rsa_obj = rsa.RSA(a=0,
                      b=16219340638145739814556409984455971733340322034588741,
                      n=19674270149491236515870218329564212980341362732018899)
    print(rsa_obj)
    
    
    print("Factoring the modulus...")
    start = time.time()
    factors = utils.factors_decomposition(rsa_obj.modulus)
    phi = (p-1)  * (q - 1) 
    # guess what are p and q ?
    end = time.time()
    print("Factorisation done in {} seconds\n".format(end - start))
    print(str(rsa_obj.modulus) + " = " + \
                        " * ".join([str(i) for i in factors]) + \
                        " = n * q ")
    print("Phi =", phi, "= (n - 1) * (q -1)")
    private = utils.inv_modulo(rsa_obj.public, phi)
    print("Private key: {}\n".format(private))

    rsa_obj.private = private
    
    print('Submit this flag:')
    print(rsa_obj.decrypt_int(332795103438906336586762421178058977844889453787945))
