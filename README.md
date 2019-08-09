# Raspberry Pi Checkout

Python script to help manage layer checkout and deployment operations for the Raspberry Pi 3 B+ OS Build. 
## Requirements

* pygit2

## Installing

The pip package manager should be used to install this tool. If you don't already have this installed, you can install pip using the following command. Pip will discover all necessary installation dependencies.

```bash
sudo apt install python-pip
```

```bash
python -m pip install rpi_checkout-0.1-py2-none-any.whl
```

## Check Out Layers

You can use the script using the following command.

```bash
python -m rpi_checkout -h
```

```
usage: rpi_checkout.py [-h] [-d DIR] -o {checkout,build,deploy}
                       [{checkout,build,deploy} ...]

optional arguments:
  -h, --help            show this help message and exit
  -d DIR, --dir DIR     Directory perform the operation to. Default is
                        /home/christopher/Documents.
  -o {checkout,build,deploy} [{checkout,build,deploy} ...], --operation {checkout,build,deploy} [{checkout,build,deploy} ...]
                        Operation to perform. Note that deploy should only be
                        used by developers.
```

