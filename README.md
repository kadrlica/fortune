Predict the future of your DECam PSF...

# Installation

Add the executable to your path:

```
> export $PATH=$PATH_TO_FORTUNE/bin:$PATH
```

# Execution

Print a help message and exit:
```
usage: fortune [-h] [-a AIRMASS] [-g] [-c [CUT]] [--ecs] [-V] fil secz psf

Predict the future of your PSF...

positional arguments:
  fil                   current DECam filter
  secz                  current airmass (secz)
  psf                   current FWHM (arcsec)

optional arguments:
  -h, --help            show this help message and exit
  -a AIRMASS, --airmass AIRMASS
                        desired airmass (secz)
  -g, --grid            return a grid of airmasses
  -c [CUT], --cut [CUT]
                        maximum acceptable FWHM (arcsec)
  --ecs                 for ECS eyes only!
  -V, --version         print version and exit.

```

Predict the PSF in the other filters:
```
> fortune g 1.4 1.4
Clear your mind and I will predict the fortune of your PSF...

Airmass:   1.40
---------------
u-band :   1.43
g-band :   1.40
r-band :   1.29
i-band :   1.24
z-band :   1.20
Y-band :   1.17
```

Specify a future airmass:
```
> fortune g 1.4 1.4 -a 1.2
Clear your mind and I will predict the fortune of your PSF...

Airmass:   1.20
---------------
u-band :   1.31
g-band :   1.28
r-band :   1.18
i-band :   1.13
z-band :   1.09
Y-band :   1.07
```

Output a grid of predicted PSFs color coded by a PSF cut:
```
> fortune g 1.4 1.4 -g --cut 1.4 
Clear your mind and I will predict the fortune of your PSF...

Airmass:   1.00   1.20   1.20   1.40   1.60   1.80   2.00
---------------------------------------------------------
u-band :   1.17   1.31   1.31   1.43   1.55   1.66   1.77
g-band :   1.14   1.28   1.28   1.40   1.52   1.63   1.73
r-band :   1.06   1.18   1.18   1.29   1.40   1.50   1.60
i-band :   1.01   1.13   1.13   1.24   1.34   1.44   1.54
z-band :   0.98   1.09   1.09   1.20   1.30   1.39   1.49
Y-band :   0.95   1.07   1.07   1.17   1.27   1.36   1.45
``