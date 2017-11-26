"""Traveler.

Script for estimating distance traveled on an image.
Path is marked using a single color.

Usage:
    traveler --image=<image> --color=<color> --scale=<scale>
    traveler -h | --help
    traveler --version

Options:
    -h --help        Show this screen.
    --version        Show version.
    --image=<image>  Image file.
    --color=<color>  Hexadecimal color without #prefix
    --scale=<scale>  Pixel scale(1 px = ??? m)
"""

import sys
from docopt import docopt

if __name__ != '__main__':
    sys.exit(1)

arguments = docopt(__doc__)
print(arguments['--image'], arguments['--color'], arguments['--scale'])
