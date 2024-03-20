#!/usr/bin/env python3

# create a list with 3 items
my_list = [ "192.168.0.5", 5060, "UP" ]

# display the first item on the list
print("The first item in the list (IP): " + my_list[0] )

# display the second item from the list
print("The second item in the list (port): " + str(my_list[1]) )

# display the last item on the list
print("The last item in the list (state): " + my_list[2] )

# Challenge portion, since it uses a different list name, I'll add it here
iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

# Now we want to display only the IP addresses here, which are numbers 3 and 4. 
print("The IP addresses from this list are " + iplist[3] + " & " + iplist[4])
# I feel like there's a better way to call for them than to go with the static list number, but I don't know it yet so this is fine for now
