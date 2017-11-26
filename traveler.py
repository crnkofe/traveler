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
import logging
from docopt import docopt
from PIL import Image

logging.basicConfig(level=logging.DEBUG)

if __name__ != '__main__':
    sys.exit(1)

arguments = docopt(__doc__)
# allowed distance from passed in color
threshold = 255 * 0.1

cr, cg, cb = int("0x" + arguments['--color'][:2], 0),\
    int("0x" + arguments['--color'][2:4], 0),\
    int("0x" + arguments['--color'][4:6], 0)

try:
    img = Image.open(arguments['--image'])
    count_same = 0
    for pixel in img.getdata():
        r, g, b = pixel[0], pixel[1], pixel[2]
        if abs(cr - r) < threshold and\
                abs(cg - g) < threshold and\
                abs(cb - b) < threshold:
            count_same += 1
    logging.info("You have travelled: %s m",
                 int(count_same * float(arguments['--scale'])))
except Exception as e:
    logging.error(e)
