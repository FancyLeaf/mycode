#!/usr/bin/python3
"""Alta3 Research | rzfeeser@alta3.com
   Learning about Python SSH
   This version incorporates the customizations/challenges"""
import paramiko
import credentials # This is the file we set our dictionary in for challenge 1
def main():
    """Our runtime code that calls other functions"""
    # harvest private key for all 3 servers
    mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")
    # Ensure our source file for IPs is referenced
    ipfile = credentials.credz

    # loop across the collection credz
    for cred in ipfile: # refer back to the variable set for the source dictionary
        ## create a session object
        sshsession = paramiko.SSHClient()
        ## add host key policy
        sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ## display our connections
        print("Connecting to... " + cred.get("un") + "@" + cred.get("ip"))
        ## make a connection
        sshsession.connect(hostname=cred.get("ip"), username=cred.get("un"), pkey=mykey)
        ## touch the file goodnews.everyone in each user's home directory
        sshsession.exec_command("touch /home/" + cred.get("un") + "/goodnews.everyone")
        ## list the contents of each home directory
        # The below is appended with an output to a file "results.log"
        sessin, sessout, sesserr = sshsession.exec_command("ls /home/ >> results.log" + cred.get("un"))
        ## display output
        print(sessout.read().decode('utf-8'))
        ## close/cleanup SSH connection
        sshsession.close()

    print("Thanks for looping with Alta3!")

main()

