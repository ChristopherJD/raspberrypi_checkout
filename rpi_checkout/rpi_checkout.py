from __future__ import print_function # Only Python 2.x
import pygit2
import argparse
import subprocess
from shutil import copy2
from os import path
from os import environ
from os import chdir
from os.path import join

HOME = environ["HOME"]
GIT_USERNAME = "git"
SSH_PUBLIC_KEY = ".ssh/id_rsa.pub"
SSH_PRIVATE_KEY = ".ssh/id_rsa"
MEGA_FILE_UPLOAD_PATH = "/home/christopher/MEGA"

def execute(cmd):
    popen = subprocess.Popen(cmd, stdout=subprocess.PIPE, universal_newlines=True)
    for stdout_line in iter(popen.stdout.readline, ""):
        yield stdout_line 
    popen.stdout.close()
    return_code = popen.wait()
    if return_code:
        raise subprocess.CalledProcessError(return_code, cmd)

class MyRemoteCallbacks(pygit2.RemoteCallbacks):

    def credentials(self, url, username_from_url, allowed_types):
        if allowed_types & pygit2.credentials.GIT_CREDTYPE_USERNAME:
            return pygit2.Username(GIT_USERNAME)
        elif allowed_types & pygit2.credentials.GIT_CREDTYPE_SSH_KEY:
            return pygit2.Keypair(GIT_USERNAME, join(HOME, SSH_PUBLIC_KEY), join(HOME, SSH_PRIVATE_KEY), "")
        else:
            return None

def checkout_operation(directory):

    # Join directories
    project_dir = directory
    poky_dir = path.join(project_dir, 'poky')
    meta_raspberrypi_dir = path.join(poky_dir, 'meta-raspberrypi')
    meta_user_dir = path.join(poky_dir, 'meta-user')
    meta_oe_dir = path.join(poky_dir, 'meta-openembedded')
    build_dir = path.join(poky_dir, 'build')

    # Print verison of libgit2
    print("LIBGIT2: {}".format(pygit2.LIBGIT2_VER))

    # Cloning order matters
    try:
        print("Cloning poky repo over http...")
        pygit2.clone_repository("https://git.yoctoproject.org/git/poky", poky_dir,
            callbacks=MyRemoteCallbacks(), checkout_branch="thud")
    except ValueError as ve:
        print("Repo already exists!")

    try:
        print("Cloning meta-raspberrypi repo over http...")
        pygit2.clone_repository("https://github.com/agherzan/meta-raspberrypi", meta_raspberrypi_dir,
            callbacks=MyRemoteCallbacks(), checkout_branch="thud")
    except ValueError as ve:
        print("Repo already exists!")

    try:
        print("Cloning build repo over http...")
        pygit2.clone_repository("https://github.com/ChristopherJD/raspberrypi_conf.git", build_dir,
            callbacks=MyRemoteCallbacks())
    except ValueError as ve:
        print("Repo already exists!")

    try:
        print("Cloning meta-user repo over http...")
        pygit2.clone_repository("https://github.com/ChristopherJD/raspberrypi_meta_user.git", meta_user_dir,
            callbacks=MyRemoteCallbacks())
    except ValueError as ve:
        print("Repo already exists!")

    try:
        print("Cloning meta-openembedded repo over http...")
        pygit2.clone_repository("https://github.com/openembedded/meta-openembedded.git", meta_oe_dir,
            callbacks=MyRemoteCallbacks(), checkout_branch="thud")
    except ValueError as ve:
        print("Repo already exists!")

    print("Please change to {} to build your project!".format(poky_dir))

def deploy_operation(directory):

    if not path.exists(directory):
        raise IOError("Directory not found!")

    os_path = path.join(directory, 'poky/build/tmp/deploy/images/raspberrypi3/rpi-basic-raspberrypi3.rpi-sdimg')
    sdk_path = path.join(directory, 'poky/build/tmp/deploy/sdk/poky-glibc-x86_64-rpi-basic-cortexa7t2hf-neon-vfpv4-toolchain-2.6.2.sh')

    if (not path.exists(os_path)) or (not path.exists(sdk_path)):
        raise IOError("File not found!")

    copy2(sdk_path, MEGA_FILE_UPLOAD_PATH)
    copy2(os_path, MEGA_FILE_UPLOAD_PATH)

def build_operation(directory):

    raise NotImplementedError("Build operation")

    # poky_dir = path.join(directory, 'poky')
    # for line in execute(["bash", "build_os.sh", poky_dir]):
    #     print(line, end="")

def main():
    
    operations = {'checkout': checkout_operation, 'deploy': deploy_operation, 'build': build_operation}
    operation_choices = operations.keys()

    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dir", help="Directory perform the operation to. Default is {}.".format(join(HOME, "Documents")), default=join(HOME, "Documents"))
    parser.add_argument("-o", "--operation", nargs='+', required=True, choices=operation_choices, default=checkout_operation, help="Operation to perform. Note that deploy should only be used by developers.")
    args = parser.parse_args()

    chosen_operations = args.operation

    try:
        for operation in chosen_operations:
            operations[operation](args.dir)
    except IOError as ioe:
        print(ioe)
    except NotImplementedError as nie:
        print("The operation is not yet supported.")

if __name__ == "__main__":
    main()
