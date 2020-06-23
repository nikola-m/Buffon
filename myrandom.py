from random import random

def rand():
    """
    Creates random number in interval [-1,1]
    """
    return (2*random()-1.0)

def ran(a,b):
    """
    Creates random number in interval [a,b]
    a,b (input) - arbitrary floats
    """
    # case 1: both a and b are positive, b>a.
    # --0-------a-----b--->
    if ( a>=0 and b>0 ):
        randNo = (b-a)*random()+a

    # case 2:a negative, b are positive, b>a.
    # --a-------0-----b--->
    elif ( a<0 and b>0 ):
        randNo = (abs(a)+b)*random()-abs(a)

    # case 3: both a and b are negative, b>a.
    # --a-------b-----0--->
    else: 
        randNo = (abs(a)-abs(b))*random()-abs(a)
    return randNo