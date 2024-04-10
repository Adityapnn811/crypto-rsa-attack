from Crypto.Util.number import * 
from factorize import factorize
from decryptRSA import decryptRSA

def decryptA(n, e, c):
    p, q = factorize(n)
    m = decryptRSA(p, q, e, c, n)
    m_string = (long_to_bytes(m))

    return(m_string)
    

def decryptB(n, e, c):
    print('decryptB')
    print(n, e, c)
    return('')


def decryptC(n, e, c):
    print('decryptC')
    print(n, e, c)
    return('')


def decryptD(n, e, c):
    print('decryptD')
    print(n, e, c)
    return('')


def decryptE(n, e, c):
    print('decryptE')
    print(n, e, c)
    return('')