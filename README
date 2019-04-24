# raspberrypi_checkout

Checkout script to get the necessary files to build raspberry pi poky OS using yocto and bitbake.

**WARNING**
This script will only work if you have the private and public SSH keys in your repository.

# Requirements

The pygit2 package is a requirement. On debian and ubuntu you can install this package with the following command.

```bash
sudo apt install python3-pygit2
```

# Checking out Files
usage: rpi_checkout.py [-h] dir

positional arguments:
  dir         Directory to checkout project to.

optional arguments:
  -h, --help  show this help message and exit

# Building Raspberry Pi image
source oe-init-build-env
bitbake rpi-basic
