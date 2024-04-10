from Crypto.Util.number import * 
from factorize import factorize
from decryptRSA import decryptRSA
from decimal import *
from cuberoot import cube_root

def decryptA(n, e, c):
    # p and q very near
    p, q = factorize(n)
    m = decryptRSA(p, q, e, c, n)
    m_string = (long_to_bytes(m))

    return(m_string)
    

def decryptB(n, e, c):
    print('decryptB')
    print(n, e, c)
    return('')


def decryptC(n, e, c):
    # e == d
    m = pow(c, e, n)
    m_string = (long_to_bytes(m))

    return(m_string)


def decryptD(n, e, c):
    # e == 3
    m = int(cube_root(c))
    m_string = (long_to_bytes(m))

    return(m_string)


def decryptE(n, e, c):
    print('decryptE')
    print(n, e, c)
    return('')