#!/usr/bin/env python3
""" Alta3 Research | Exploring interfaces today
    Student: Michael Carter (Github: FancyLeaf) """
# Importing netifaces so we can use these tools
import netifaces

# Bonus challenge functions
def find_ip(interface_name):
    return (netifaces.ifaddresses(interface_name)[netifaces.AF_INET][0]['addr'])

def find_mac(interface_name):
    return (netifaces.ifaddresses(interface_name)[netifaces.AF_LINK][0]['addr'])

# Main function!
def main():
    for i in netifaces.interfaces():
            print('\n**************Details of Interface - ' + i + ' *********************')
            try:
                print('MAC: ', find_mac(i))
                print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])
                print('IP: ', find_ip(i))
                print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])
            except:
                print('Could not collect adapter information')

if __name__ == "__main__":
    main()
