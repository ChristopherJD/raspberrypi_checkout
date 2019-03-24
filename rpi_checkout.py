#!/usr/bin/env python3
import pygit2
import argparse
from os import path


class MyRemoteCallbacks(pygit2.RemoteCallbacks):

    # TODO these credentials are bogus, don't even know we need this, but leave
    # as an example for now
    def credentials(self, url, username_from_url, allowed_types):
        if allowed_types & pygit2.credentials.GIT_CREDTYPE_USERNAME:
            return pygit2.Username("git")
        elif allowed_types & pygit2.credentials.GIT_CREDTYPE_SSH_KEY:
            return pygit2.Keypair("git", "id_rsa.pub", "id_rsa", "")
        else:
            return None

def main():

    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("dir", help="Directory to checkout project to.")
    args = parser.parse_args()

    # Join directories
    project_dir = args.dir
    poky_dir = path.join(project_dir, 'poky')
    meta_raspberrypi_dir = path.join(poky_dir, 'meta-raspberrypi')
    meta_user_dir = path.join(poky_dir, 'meta-user')
    build_dir = path.join(poky_dir, 'build')

    # Print verison of libgit2
    print("LIBGIT2: {}".format(pygit2.LIBGIT2_VER))

    # Cloning order matters
    print("Cloning poky repo over http...")
    pygit2.clone_repository("https://git.yoctoproject.org/git/poky", poky_dir,
        callbacks=MyRemoteCallbacks(), checkout_branch="thud")

    print("Cloning meta-raspberrypi repo over http...")
    pygit2.clone_repository("https://github.com/agherzan/meta-raspberrypi", meta_raspberrypi_dir,
        callbacks=MyRemoteCallbacks(), checkout_branch="thud")

    print("Cloning build repo over http...")
    pygit2.clone_repository("https://github.com/ChristopherJD/raspberrypi_conf", build_dir,
        callbacks=MyRemoteCallbacks())

    print("Cloning meta-user repo over http...")
    pygit2.clone_repository("https://github.com/ChristopherJD/raspberrypi_meta_user", build_user,
        callbacks=MyRemoteCallbacks())

if __name__ == "__main__":
    main()
