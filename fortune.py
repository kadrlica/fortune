#!/usr/bin/env python
"""
Predict the future of your PSF...
"""
__version__ = '1.1'

import os
from collections import OrderedDict as odict

BANDS = ['u','g','r','i','z','Y']
GRID = [1.0, 1.2, 1.4, 1.6, 1.8, 2.0]

# These were empirically derived to minimize the bias
LAMBDA = odict([
    ('u',380.),
    ('g',425.),
    ('r',630.),
    ('i',780.),
    ('z',920.),
    ('Y',1050.),
])

# These come from the original filter curves
LAMBDA_ORIG = odict([
    ('u',380.),
    ('g',480.),
    ('r',640.),
    ('i',780.),
    ('z',920.),
    ('Y',990.),
])

COLORS = odict([
   ('PURPLE'   ,'\033[95m'),
   ('CYAN'     ,'\033[96m'),
   ('DARKCYAN' ,'\033[36m'),
   ('BLUE'     ,'\033[94m'),
   ('GREEN'    ,'\033[92m'),
   ('YELLOW'   ,'\033[93m'),
   ('RED'      ,'\033[91m'),
   ('BOLD'     ,'\033[1m'),
   ('UNDERLINE','\033[4m'),
   ('END'      ,'\033[0m'),
])

MAX = None
COLOR = False

def color(s,color):
    color = color.upper()
    # This is not the best way to check for color support.
    # Look into 'tput colors'...
    if 'xterm' not in os.getenv('TERM'):
        return s
    elif not COLOR:
        return s
    else:
        return COLORS[color] + s + COLORS['END']

def fwhm(fwhm_now, lambda_now, secz_now, lambda_next, secz_next):
    """Predict the fwhm.

    Parameters:
    -----------
    fwhm_now    : The fwhm value of the current exposure
    lambda_now  : The wavelength of the current exposure
    secz_now    : The airmass of the current exposure
    lambda_next : The wavelength of the next exposure
    secz_next   : The airmass of the next exposure
    
    Returns:
    --------
    fwhm_next   : The predicted fwhm of the next exposure
    """
    lambda_now, secz_now = map(float,[lambda_now, secz_now])
    lambda_next, secz_next = map(float,[lambda_next, secz_next])
    fwhm_next = fwhm_now * (lambda_next/lambda_now)**(-0.2) * (secz_next/secz_now)**(0.6)
    return fwhm_next

def fortune(fwhm_now, band_now, secz_now, secz_next=None):
    """Print the fwhm prediction.
    
    Parameters:
    -----------
    fwhm_now :
    band_now :
    secz_now :
    secz_next :
    
    Returns:
    --------
    None
    """
    lambda_now = LAMBDA[band_now]

    if secz_next is None:
        secz_next = [secz_now]
    elif isinstance(secz_next,(float,int,str)):
        secz_next = [secz_next]

    secz_next = sorted(secz_next)

    intro = "Clear your mind and I will predict the fortune of your PSF...\n"
    print(intro)

    header = "%-7s:"%"Airmass"+''.join(['%7.2f'%s for s in secz_next])
    print(header)

    hline = len(header)*"-"
    print(hline)

    good = False
    terrible = True
    future = []
    for b in BANDS:
        out = "%-7s:"%('%s-band'%b)
        for i,secz in enumerate(secz_next):
            lambda_next = LAMBDA[b]
            fwhm_next = fwhm(fwhm_now,lambda_now, secz_now, lambda_next, secz)
            fwhm_str = '%7.2f'%fwhm_next
            future.append(fwhm_next)

            if fwhm_next < 3.0:
                terrible = False
            if MAX is not None:
                if fwhm_next > MAX:
                    out += color(fwhm_str,'red')
                else:
                    out += color(fwhm_str,'darkcyan')
                    good = True
            else:
                out += fwhm_str

        print(out)

    if max(future) < 1.1:
        msg = '\n' + color('Your future is bright!','bold')
        print(msg)
    elif min(future) > 3.0:
        msg = '\n' + color('Your future is bleak. Close the dome and go home.','bold')
        print(msg)
    elif min(future) > (MAX if MAX else 2.0):
        msg = '\n' + color('Your future is murky.','bold')
        print(msg)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('band',choices=BANDS,metavar='fil',
                        help='current DECam filter')
    parser.add_argument('secz',default=None,type=float,
                        help='current airmass (secz)')
    parser.add_argument('psf',default=None,type=float,
                        help='current FWHM (arcsec)')
    parser.add_argument('-a','--airmass',default=None,action='append',
                        type=float,help='desired airmass (secz)')
    parser.add_argument('-g','--grid',default=None,action='store_true',
                        help='return a grid of airmasses')
    parser.add_argument('-c','--cut',nargs='?',const=1.1,
                        default=None,type=float,
                        help='maximum acceptable FWHM (arcsec)')
    parser.add_argument('--ecs',action='store_true',
                        help='for ECS eyes only!')
    parser.add_argument('-V','--version',action='version',
                        version='%(prog)s '+__version__,
                        help='print version and exit.')

    args = parser.parse_args()
    MAX   = args.cut
    COLOR = args.cut

    if args.airmass: airmass = args.airmass
    else:            airmass = [args.secz]
    if args.grid:    airmass += GRID
        
    fortune(args.psf,args.band,args.secz,airmass)

    if args.ecs:
        print('\n'+color("You're the best!",'bold'))
