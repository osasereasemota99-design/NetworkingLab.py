# Osasere Asemota

import os
import datetime


date = datetime.datetime.now().strftime("%Y-%m-%d")
file = date + "Osasere_network.txt"

print("Network Info")
print("Date:", date)
print("Test: google.com")

f = open(file, "w")
f.write("Network Info\n")
f.write("Date: " + date + "\n")
f.write("Testing: google.com\n")

print("\nHostname:")
os.system("hostname")
f.write("\nHostname:\n")
os.system("hostname >> " + file)

print("\nIP Address:")
os.system("hostname -I")
f.write("\nIP Address:\n")
os.system("hostname -I >> " + file)

print("\nRouting:")
os.system("ip route")
f.write("\nRouting:\n")
os.system("ip route >> " + file)

print("\nPing Test:")
os.system("ping -c 4 google.com")
f.write("\nPing Test:\n")
os.system("ping -c 4 google.com >> " + file)

print("\nTracepath:")
os.system("tracepath google.com")
f.write("\nTracepath:\n")
os.system("tracepath google.com >> " + file)

print("\nNetplan Files:\n")
os.system("ls /etc/netplan/")
f.write("\nNetplan Files:\n")
os.system("ls /etc/netplan/ >> " + file)

f.close()

print("\nSaved to:", file)