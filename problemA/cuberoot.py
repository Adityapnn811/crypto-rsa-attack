# https://stackoverflow.com/questions/47191533/how-to-efficiently-calculate-cube-roots-using-decimal-in-python
from decimal import *

def cube_root( A): 
    getcontext().prec = 2048
    d1 = Decimal(1)
    d2 = Decimal(2)
    d3 = Decimal(3)

    x0 = (A-d1)/d3
    xn = (d2 * x0 + A / Decimal(x0*x0) ) / d3

    while xn != x0:
        x0 = xn
        xn = (d2 * x0 + A / Decimal(x0*x0) ) / d3

    return xn