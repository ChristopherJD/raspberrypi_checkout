# raspberrypi_checkout

Checkout script to get the necessary files to build raspberry pi poky OS using yocto and bitbake.

# Requirements

It is required to use the pip package manager. You can install using the following command.

```bash
sudo apt install python-pip3
```

# Installing

```bash
pip3 install .
```

# Checking out Files

You can use the script using the following command.

```bash
python3 -m rpi_checkout
```

usage: __main__.py [-h] [-d DIR]

optional arguments:
  -h, --help         show this help message and exit
  -d DIR, --dir DIR  Directory to checkout project to. Default is
                     $HOME/Documents. WARNING you must change your layers
                     listed in build/conf/bblayers.conf if you are going to
                     use this option.

# Building Raspberry Pi image
source oe-init-build-env
bitbake rpi-basic