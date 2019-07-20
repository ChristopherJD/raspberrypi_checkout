# Raspberry Pi Checkout

Python script to help manage code checkout and deployment operations for the Raspberry Pi. This project runs the poky distro from the Yocto system as its operating system. This includes a custom set of libraries and tools.

## Pre-Build Images and SDK

**SDK**

You can download the pre-built SDK [here](https://mega.nz/#!YP4DjShJ!588wAkehnsjxvIR2CdM7gWTSWsFwzVhFdL5ZB3e0OUU).

**Raspberry Pi SD Card Image**

You can downlaod the pre-build image [here](https://mega.nz/#!dT5zXCZI!U9SByom1hd35hkGbRb1zY7k88gR4W27ogGxhx_gNBP4)

## Requirements

* pygit2

## Installing

The pip package manager should be used to install this tool.

```bash
sudo apt install python-pip
```

```bash
pip install .
```

## Checking out Files

You can use the script using the following command.

```bash
python -m rpi_checkout
```

```
usage: __main__.py [-h] [-d DIR]

optional arguments:
  -h, --help         show this help message and exit
  -d DIR, --dir DIR  Directory to checkout project to. Default is
                     $HOME/Documents. WARNING you must change your layers
                     listed in build/conf/bblayers.conf if you are going to
                     use this option.
```

## Building Raspberry Pi image

### Setup

(Required) However it is recommended that you either change the location that yocto uses for package download, or mount an external hard drive as I have done to store these packages.

**Adding an External Hard Drive**

The following steps will cause your hard drive to be mounted automatically at startup.

1. Create a directory to mount the hard drive.

    ```bash
    sudo mkdir /media/external_500
    sudo chown -R $(id -u):$(id -u) /media/external_500/
    ```

1. Check the UUID of the hard drive to add to the fstab file.

    ```bash
    sudo blkid
    ```

1. Append the device to the `/etc/fstab` file. Please note that you should replace your UUID with the one found in the above command. Below is only to be used as reference.

    ```bash
    UUID=bc3040c9-ae5a-4ffc-93ab-466ca2444616 /media/external_500 ext4 rw,auto,nofail 0 0
    ```
  
**Change the Configuration**

1. You must first checkout the project.

    ```bash
    python -m rpi_checkout -o checkout
    ```
  
1. Change into the build configuration directory.

    ```bash
    cd ~/Documents/poky/build/conf
    ```
  
1. Edit the `conf/local.conf` file.

Old:

```
DL_DIR ?= "/media/external_500/downloads"
SSTATE_DIR ?= "/media/external_500/sstate-cache"
```
  
New:

```
DL_DIR ?= "${TOPDIR}/downloads"
SSTATE_DIR ?= "${TOPDIR}/sstate-cache"
```
  
### Building

1. Checkout the necessary files (If not previously competed). Please note this could take some time (depends on size of repo).

    ```bash
    python -m rpi_checkout -o checkout
    ```

1. Change to the poky build directory and source the build environment.

    ```bash
    source oe-init-build-env
    ```
  
1. Run the bitbake command and build the poky OS. The build process is lengthy for the first build, however once the cache is built it should significantly reduce the time to build.

    ```bash
    bitbake rpi-basic
    ```
