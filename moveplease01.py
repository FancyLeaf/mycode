#!/usr/bin/env python3
""" Python course - Lab 29 | Completed with extreme prejudice by FancyLeaf
    This is for lab 29, moving and copying files """

# Import some stuff here so we can move and copy files
import shutil
import os

def main():
    # Change directory to the appropriate
    os.chdir('/home/student/mycode/')

    # Moving Raynor back to the correct place
    shutil.move('raynor.obj', 'ceph_storage/')

    # Renaming an existing file based on input/variables
    xname = input('What is the new name for kerrigan.obj? ')
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

if __name__ == "__main__":
    main()
