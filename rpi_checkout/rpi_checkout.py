import pygit2
import argparse
from os import path
from os import environ
from os.path import join

HOME = environ["HOME"]
GIT_USERNAME = "git"
SSH_PUBLIC_KEY = ".ssh/id_rsa.pub"
SSH_PRIVATE_KEY = ".ssh/id_rsa"


class MyRemoteCallbacks(pygit2.RemoteCallbacks):

    def credentials(self, url, username_from_url, allowed_types):
        if allowed_types & pygit2.credentials.GIT_CREDTYPE_USERNAME:
            return pygit2.Username(GIT_USERNAME)
        elif allowed_types & pygit2.credentials.GIT_CREDTYPE_SSH_KEY:
            return pygit2.Keypair(GIT_USERNAME, join(HOME, SSH_PUBLIC_KEY), join(HOME, SSH_PRIVATE_KEY), "")
        else:
            return None

def main():

    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dir", help="Directory to checkout project to. Default is $HOME/Documents. WARNING you must change your layers listed in build/conf/bblayers.conf if you are going to use this option.", default=join(HOME, "Documents"))
    args = parser.parse_args()

    # Join directories
    project_dir = args.dir
    poky_dir = path.join(project_dir, 'poky')
    meta_raspberrypi_dir = path.join(poky_dir, 'meta-raspberrypi')
    meta_user_dir = path.join(poky_dir, 'meta-user')
    meta_oe_dir = path.join(poky_dir, 'meta-openembedded')
    build_dir = path.join(poky_dir, 'build')

    # Print verison of libgit2
    # print("LIBGIT2: {}".format(pygit2.LIBGIT2_VER))

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
        print("Cloning build repo over ssh...")
        pygit2.clone_repository("git@github.com:ChristopherJD/raspberrypi_conf.git", build_dir,
            callbacks=MyRemoteCallbacks())
    except ValueError as ve:
        print("Repo already exists!")

    try:
        print("Cloning meta-user repo over ssh...")
        pygit2.clone_repository("git@github.com:ChristopherJD/raspberrypi_meta_user.git", meta_user_dir,
            callbacks=MyRemoteCallbacks())
    except ValueError as ve:
        print("Repo already exists!")

    try:
        print("Cloning meta-openembedded repo over http...")
        pygit2.clone_repository("https://github.com/openembedded/meta-openembedded.git", meta_oe_dir,
            callbacks=MyRemoteCallbacks(), checkout_branch="thud")
    except ValueError as ve:
        print("Repo already exists!")

