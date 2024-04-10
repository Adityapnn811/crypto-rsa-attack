from decimal import *
from sympy import nextprime 

def factorize (num):
  getcontext().prec = 1024
  p = int(Decimal(num).sqrt())

  while (p < num and num % p != 0):
    p = nextprime(p)
  
  return (p, num//p)