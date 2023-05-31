from pathlib import Path
import netifaces
import re
import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

path = Path(myDir)
a = str(path.parent.absolute())
sys.path.append(a)
from data.ifaces import ifaces


pattern = r"^(?:\d{1,3}\.){3}\d{1,3}$"


def ipv4_helper(interface):
    addrs = netifaces.ifaddresses(interface)
    print("addrs", addrs)
    if netifaces.AF_INET in addrs:
        return addrs[netifaces.AF_INET][0]['addr']
    print(addrs[netifaces.AF_INET][0]['addr'])
    return None

  # Example list of interfaces

# provides the ipv4 addr and interface 
def get_ipv4_addr(list):
    pattern = r"^(?:\d{1,3}\.){3}\d{1,3}$"
    for interface in list:
        try:
            interface_ip = ipv4_helper(interface)
            if interface_ip and re.match(pattern, interface_ip):
                return interface_ip
            else:
                print(
                    f"Invalid IPv4 address for {interface}: {interface_ip}")
            break
        except:
            pass

# provides the ipv4 addr and interface 
def get_interface(list):
    pattern = r"^(?:\d{1,3}\.){3}\d{1,3}$"
    for interface in list:
        try:
            interface_ip = ipv4_helper(interface)
            if interface_ip and re.match(pattern, interface_ip):
                return interface
            else:
                print(
                    f"Invalid IPv4 address for {interface}: {interface_ip}")
        except:
            pass

x = get_interface(ifaces)
y = get_ipv4_addr(ifaces)
print(x)
print(y)
# get_interface is the funcion to import 

'''
LEFTOFF
TODO - Create functions that return (the printed values)
TODO - integrate this functionality into the host options gui box
'''