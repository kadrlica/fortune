Predict the future of your DECam PSF...

# Installation

Add the executable to your path:

```
> export $PATH=$PATH_TO_FORTUNE/bin:$PATH
```

# Execution

Print a help message and exit:
```
> fortune --help
usage: fortune [-h] -p PSF -b {u,g,r,i,z,Y} -a AIRMASS [-f FUTURE] [-m MAX]
               [-e] [-V]

Predict the future of your PSF...

optional arguments:
  -h, --help            show this help message and exit
  -p PSF, --psf PSF     current FWHM (arcsec)
  -b {u,g,r,i,z,Y}, --band {u,g,r,i,z,Y}
                        current DECam band
  -a AIRMASS, --airmass AIRMASS
                        current airmass (secz)
  -f FUTURE, --future FUTURE
                        future airmass (secz)
  -m MAX, --max MAX     maximum acceptable FWHM (arcsec)
  -e, --ecs             for ECS only!!!
  -V, --version         print version and exit.
```

Create a grid of predicted PSFs based on the current psf (`--psf`), band (`--band`), and airmass (`--airmass`):
```
> fortune --psf 1.4 --band g --airmass 1.4
Clear your mind and I will predict your future...

Airmass:    1.0    1.2    1.4    1.6    1.8    2.0
--------------------------------------------------
u-band :   1.20   1.34   1.47   1.59   1.71   1.82
g-band :   1.14   1.28   1.40   1.52   1.63   1.73
r-band :   1.08   1.20   1.32   1.43   1.54   1.64
i-band :   1.04   1.16   1.27   1.38   1.48   1.57
z-band :   1.00   1.12   1.23   1.33   1.43   1.52
Y-band :   0.99   1.10   1.21   1.31   1.41   1.50
```

Specify a future airmass:
```
> fortune --psf 1.4 --band g --airmass 1.4 --future 1.2
Clear your mind and I will predict your future...

Airmass:    1.2
---------------
u-band :   1.34
g-band :   1.28
r-band :   1.20
i-band :   1.16
z-band :   1.12
Y-band :   1.10
```

Specify a desired PSF:
```
> ./fortune --psf 1.4 --band g --airmass 1.4 --max 1.4
Clear your mind and I will predict your future...

Airmass:    1.0    1.2    1.4    1.6    1.8    2.0
--------------------------------------------------
u-band :   1.20   1.34   1.47   1.59   1.71   1.82
g-band :   1.14   1.28   1.40   1.52   1.63   1.73
r-band :   1.08   1.20   1.32   1.43   1.54   1.64
i-band :   1.04   1.16   1.27   1.38   1.48   1.57
z-band :   1.00   1.12   1.23   1.33   1.43   1.52
Y-band :   0.99   1.10   1.21   1.31   1.41   1.50
```

# Credits

Marisa March, Ting Li, Alex Drlica-Wagner