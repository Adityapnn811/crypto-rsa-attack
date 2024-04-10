from Crypto.Util.number import * 
from factorize import factorize
from decryptRSA import decryptRSA
from decimal import *
from cuberoot import cube_root

def decryptA(n, e, c):
    # p and q very near
    p, q = factorize(n)
    m = decryptRSA(p, q, e, c, n)
    m_bytes = (long_to_bytes(m))

    return(m_bytes)
    

def decryptB(n, e, c):
    # p == q
    getcontext().prec = 1024
    p = int(Decimal(n).sqrt()) # p = q = sqrt(n)
    # TODO: find out why phi is (p)*(p - 1) instead of (p-1)*(p-1)
    phi = (p)*(p - 1)
    d = inverse(e, phi)
    m = pow(c, d, n)
    m_bytes = (long_to_bytes(m))

    return(m_bytes)


def decryptC(n, e, c):
    # e == d
    m = pow(c, e, n)
    m_bytes = (long_to_bytes(m))

    return(m_bytes)


def decryptD(n, e, c):
    # e == 3
    m = int(cube_root(c))
    m_bytes = (long_to_bytes(m))

    return(m_bytes)


def decryptE(n, e, c):
    # n is prime
    phi = n-1
    d = inverse(e, phi)
    m = pow(c, d, n)
    m_bytes = (long_to_bytes(m))

    return(m_bytes)