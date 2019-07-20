WORKING_DIR=$1

cd ${WORKING_DIR}

source ./oe-init-build-env

cd build

pwd

bitbake rpi-basic
bitbake rpi-basic -c populate_sdk
