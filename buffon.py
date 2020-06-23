from math import pi,cos,sin
from myrandom import ran
from pypostscript import BuffonFig

def buffon_needle_exp(a,b):
    '''Implements Buffon's experiment for needles of length a, on a reduced pad,
    0 < phi < pi/2
    0 < x < b/2.
    Where b is distance between the grid lines and a <= b. 

    Input:
    a - float, length of the needle
    b - float, distance between the lines.
    '''
    hit = False

    # Sizes sp needle can land to prespecified grid in .ps file
    # 
    xc = ran(0,475)
    yc = ran(0,700)
    angle = ran(0,360)

    rad = angle/360*2*pi

    # Check where the needle tip is at.    
    xtip = xc + (a/2)*cos(rad)

    # Position of the eye of the needle
    xeye = xc - (a/2.)*cos(rad)  
    yeye = yc - (a/2.)*sin(rad)  

    # Test sa narednom linijom
    stripe = xc//b + 1

    if ( (xtip-stripe*b) < 0 and (xeye-stripe*b) > 0 ):
        hit = True
    elif ( (xtip-stripe*b) > 0 and (xeye-stripe*b) < 0 ):
        hit = True

    # Test sa prethodnom linijom
    stripe = xc//b

    if ( (xtip-stripe*b) < 0 and (xeye-stripe*b) > 0 ):
        hit = True
    elif ( (xtip-stripe*b) > 0 and (xeye-stripe*b) < 0 ):
        hit = True

    # print(stripe, angle, (xtip-stripe*b), (xeye-stripe*b) )

    return xeye,yeye,angle,hit

if __name__ == '__main__':
    
    num_needles = int( input('Number of needles: ') )

    fig = BuffonFig('buffon-experiment-fig', num_needles)

    b = 25
    a = b

    Nhits = 0

    for i in range( num_needles ):
        xo,yo,angle,hit = buffon_needle_exp( a,b )
        fig.addNeedle(xo,yo,angle,hit)
        if hit:
            Nhits += 1

    fig.addText('Times-Roman',12,0,-20,"Number of hits: "+str(Nhits)+". Estimated value of pi: " + str(2*num_needles/float(Nhits)) ) 
    fig.save()

    print('Simulation over!')


