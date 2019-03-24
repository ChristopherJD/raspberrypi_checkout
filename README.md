# raspberrypi_checkout

Checkout script to build raspberry pi poky OS using yocto and bitbake.

# Checking out Files
usage: rpi_checkout.py [-h] dir

positional arguments:
  dir         Directory to checkout project to.

optional arguments:
  -h, --help  show this help message and exit

# Building Raspberry Pi image
source oe-init-build-env
bitbake rpi-basic
