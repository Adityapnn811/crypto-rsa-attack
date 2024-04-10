from Crypto.Util.number import * 

p = 47
q = 71
e = 79
# m = "KRIPTOGRAFIITB{gws}"
m = 2671

# ENCRYPTION
n = p*q
phi = (p-1)*(q-1)
d = inverse(e, phi)
print("d = ", d)
print()
c = pow(m, e, n)
print("c = ", c)
print()

# DECRYPTION
m_dec = pow(c, d, n)
print("m_dec = ", m_dec)
print()