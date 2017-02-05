#!/usr/bin/env python
"""
Predict the future of your PSF...
"""
__version__ = '1.0'

import os
from collections import OrderedDict as odict

BANDS = odict([
    ('u',380),
    ('g',480),
    ('r',640),
    ('i',780),
    ('z',920),
    ('Y',990),
])

COLORS = odict([
   ('PURPLE'  ,'\033[95m'),
   ('CYAN'    ,'\033[96m'),
   ('DARKCYAN','\033[36m'),
   ('BLUE'    ,'\033[94m'),
   ('GREEN'   ,'\033[92m'),
   ('YELLOW'  ,'\033[93m'),
   ('RED'     ,'\033[91m'),
   ('BOLD'    ,'\033[1m'),
   ('UNDERLINE','\033[4m'),
   ('END'     ,'\033[0m'),
])

MAX = None

def color(s,color):
    color = color.upper()
    # This is not the best way to check for color support.
    # Look into 'tput colors'...
    if 'xterm' in os.getenv('TERM'):
        return COLORS[color] + s + COLORS['END']
    else:
        return s

def fwhm(fwhm_now, lambda_now, secz_now, lambda_future, secz_future):
    lambda_now, secz_now, lambda_future, secz_future = map(float,[lambda_now, secz_now, lambda_future, secz_future])
    fwhm_future = fwhm_now * (lambda_future/lambda_now)**(-0.2) * (secz_future/secz_now)**(0.6)
    return fwhm_future

def fortune(fwhm_now, band_now, secz_now, secz_future=None):
    lambda_now = BANDS[band_now]

    if secz_future is None:
        secz_future = [1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
    elif isinstance(secz_future,(float,int,str)):
        secz_future = [secz_future]
    secz_future = sorted(secz_future)

    intro = "Clear your mind and I will predict your future...\n"
    print(intro)

    header = "%-7s:"%"Airmass"+''.join(['%7.1f'%s for s in secz_future])
    print(header)

    hline = len(header)*"-"
    print(hline)

    good = False
    terrible = True
    future = []
    for b in BANDS:
        out = "%-7s:"%('%s-band'%b)
        for i,secz in enumerate(secz_future):
            lambda_future = BANDS[b]
            fwhm_future = fwhm(fwhm_now,lambda_now, secz_now, lambda_future, secz)
            fwhm_str = '%7.2f'%fwhm_future
            future.append(fwhm_future)

            if fwhm_future < 3.0:
                terrible = False
            if MAX is not None:
                if fwhm_future > MAX:
                    out += color(fwhm_str,'red')
                else:
                    out += color(fwhm_str,'green')
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
    parser.add_argument('-p','--psf',required=True,default=None,type=float,
                        help='current FWHM (arcsec)')
    parser.add_argument('-b','--band',required=True,choices=BANDS.keys(),
                        help='current DECam band')
    parser.add_argument('-a','--airmass',required=True,default=None,type=float,
                        help='current airmass (secz)')
    parser.add_argument('-f','--future',default=None,action='append',type=float,
                        help='future airmass (secz)')
    parser.add_argument('-m','--max',default=None,type=float,
                        help='maximum acceptable FWHM (arcsec)')
    parser.add_argument('-e','--ecs',action='store_true',
                        help='for ECS only!!!')
    parser.add_argument('-V','--version',action='version',version='%(prog)s '+__version__,
                        help='print version and exit.')

    args = parser.parse_args()
    MAX = args.max
    fortune(args.psf,args.band,args.airmass,args.future)

    if args.ecs:
        print('\n'+color("You're the best!",'bold'))
