# Osasere Asemota
# Server Troubleshooting Menu

import os

while True:
    print("\nWhat server are you using?")
    print("1. Ubuntu Server")
    print("2. CentOS Server")
    print("3. Exit")

    server = input("Pick 1, 2, or 3: ")

    if server == "3":
        print("Goodbye")
        break

    if server == "1":
        server_name = "Ubuntu"
    elif server == "2":
        server_name = "CentOS"
    else:
        print("Invalid choice")
        continue

    print("\nYou picked:", server_name)

    print("\nTroubleshooting Suggestions:")
    print("1. Check if the system has an IP address.")
    print("Command: hostname -I")

    print("\n2. Check the routing table and default gateway.")
    print("Command: ip route")

    print("\n3. Test internet connectivity.")
    print("Command: ping -c 4 google.com")

    print("\n4. Trace the path to google.com.")
    print("Command: tracepath google.com")

    print("\n5. Check open network connections.")
    print("Command: ss -tuln")

    if server_name == "Ubuntu":
        print("\nUbuntu Static IP / DNS Help:")
        print("Ubuntu uses netplan files in /etc/netplan/")
        print("Check files with: ls /etc/netplan/")
        print("View config with: sudo cat /etc/netplan/*.yaml")
        print("Apply changes with: sudo netplan apply")

    if server_name == "CentOS":
        print("\nCentOS Static IP / DNS Help:")
        print("CentOS often uses NetworkManager.")
        print("Check connections with: nmcli connection show")
        print("Set DNS with: sudo nmcli connection modify [name] ipv4.dns 8.8.8.8")
        print("Restart connection with: sudo nmcli connection up [name]")

    input("\nPress Enter to go back to the main menu...")