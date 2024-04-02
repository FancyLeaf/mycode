from netmiko import ConnectHandler
# Defining our new function "bootstrapper", and expected arguments.
def bootstrapper(dev_type, dev_ip, dev_un, dev_pw, config):
    try:
        config_file = open(config, "r") # Opening file object described by config
        config_lines = config_file.read().splitlines() # Creating a list of file lines without \n
        config_file.close() #Closing said file object
        open_connection = ConnectHandler(device_type=dev_type, ip=dev_ip, username=dev_un, password=dev_pw)
        open_connection.enable() # Enabling connection mode
        # Passing config to "send_config_set()" method
        output = open_connection.send_config_set(config_lines)
        print(output) # Printing output to screen
        open_connection.send_command_expect('write memory')
        open_connection.disconnect() # Closing our open connection
        return True # If everything worked, we're good.
    except:
        return False # If something didn't work
