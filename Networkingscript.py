# Osasere Asemota

import os
import datetime

# Get current date in YYYY-MM-DD 
date = datetime.datetime.now().strftime("%Y-%m-%d")
# Creates a file name using the date and my name
file = date + "Osasere_network.txt"

# Header info screen
print("Network Info")
print("Date:", date)
print("Test: google.com")

# Open file in write mode creates file
f = open(file, "w")
f.write("Network Info\n")
f.write("Date: " + date + "\n")
f.write("Testing: google.com\n")

# Show and save hostname (system name)
print("\nHostname:")
os.system("hostname")
f.write("\nHostname:\n")
os.system("hostname >> " + file)

# Show and save IP address of system
print("\nIP Address:")
os.system("hostname -I")
f.write("\nIP Address:\n")
os.system("hostname -I >> " + file)

# show and save routing 
print("\nRouting:")
os.system("ip route")
f.write("\nRouting:\n")
os.system("ip route >> " + file)

# Ping test to check internet connection
print("\nPing Test:")
os.system("ping -c 4 google.com")
f.write("\nPing Test:\n")
os.system("ping -c 4 google.com >> " + file)


# Trace path to show route packets
print("\nTracepath:")
os.system("tracepath google.com")
f.write("\nTracepath:\n")
os.system("tracepath google.com >> " + file)

# Show and save netplan configuration files
print("\nNetplan Files:\n")
os.system("ls /etc/netplan/")
f.write("\nNetplan Files:\n")
os.system("ls /etc/netplan/ >> " + file)

# Close file after writing
f.close()

# Let user know where file was saved
print("\nSaved to:", file)
