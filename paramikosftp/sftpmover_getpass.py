#!/usr/bin/python3
## Try a real world test with getpass

## import Paramiko so we can talk SSH
import paramiko # allows Python to ssh
import os # low level operating system commands
import getpass # we need this to accept passwords


def transfertodir():
    """ This is for the challenge portion of lab 58"""
    while True:
        what_dir = input("Where are you slapping them? (default-/tmp/) ")
        if what_dir =="":
            what_dir = "/tmp/"
            break
        elif what_dir[0] == "/" and what_dir[-1] == "/":
            break
        print("You must enter a full path for the host fam, those start and end with "/"")
    return what_dir

def slappemthere(sftp):
    """ Moves files from A to B in a SFTP Paramiko channel """
    what_dir = transfertodir()
    for this in os.listdir("/home/student/filestocopy/"):
        if not os.path.isdir("home/student/filestocopy/"+this):
            sftp.put("/home/student/filestocopy/"+this, what_dir+this)
    return

def main():
    ## where to connect to
    t = paramiko.Transport("10.10.2.3", 22) ## IP and port of bender
    
    ## how to connect (see other labs on using id_rsa private / public keypairs)
    t.connect(username="bender", password=getpass.getpass()) # notice the password references getpass
    
    ## Make an SFTP connection object
    sftp = paramiko.SFTPClient.from_transport(t)
    
    # The movement phase
    slappemthere(sftp)
    
    ## close the connection
    sftp.close() # close the connection
    t.close() # Closes transport channel

if __name__ == "__main__":
    main()

