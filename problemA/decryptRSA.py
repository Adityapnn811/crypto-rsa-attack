from Crypto.Util.number import * 

def decryptRSA(p, q, e, c, n):
    phi = (p - 1)*(q - 1)
    d = inverse(e, phi)
    m = pow(c, d, n)
    return(m)