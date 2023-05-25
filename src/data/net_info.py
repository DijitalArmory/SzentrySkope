import socket
import netifaces
import ipaddress


def host_name(self):
    return socket.gethostname() # localhost




def get_ip_addr():
    # Get the IP address associated with the hostname
    ip_address = socket.gethostbyname(socket.gethostname())
    return ip_address


def get_default_gateway():
    """
    Returns the default gateway of the current system.
    """
    gws = netifaces.gateways()
    return gws['default'][netifaces.AF_INET][0]

# TODO: have user assign the parameter (interface) with a radio button 5/5/23
def get_network_addr(interface):
    """
    Returns the network address and subnet mask of the specified network interface.
    """
    # Get the addresses associated with the specified interface
    addrs = netifaces.ifaddresses(interface)
    # Extract the IPv4 address and subnet mask
    ip = addrs[netifaces.AF_INET][0]['addr']
    netmask = addrs[netifaces.AF_INET][0]['netmask']
    # Calculate the network address from the IP address and subnet mask
    network = ipaddress.IPv4Network((ip, netmask), strict=False)
    return network


ipv4 = get_ip_addr()
network = get_network_addr("enp0s3")
ipv4_gateway = str(network.network_address)
netmask = str(network.netmask)