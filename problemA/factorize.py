from decimal import *
from sympy import nextprime 

def factorize (num):
  getcontext().prec = 2048
  p = int(Decimal(num).sqrt())

  while (p < num and num % p != 0):
    p = nextprime(p)
  
  return (p, num//p)