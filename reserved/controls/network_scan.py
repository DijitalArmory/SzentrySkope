import subprocess
import os
from data.net_info import (get_ip_addr, get_default_gateway, get_network_addr)
#from data.net_scan_constants import *
from data.path_constants import ROOT_TO_SOURCE
from data.file_constants import SCAN_RESULTS_FILE
from parsers.netScanResParse import process_lines, replace_file
import time


# TODO: have user assign the parameter (interface) with a radio button 5/5/23
# Replace "eth0" with the name of the network interface you want to retrieve information for

def generate_scan_results_file(file_new, port_scan):
      with open(file_new, "w") as scanResults:
        res = scanResults.write(port_scan.stdout.decode())
        print(res)
        

# network scan function
def net_scan(list):
    port_scan = subprocess.run(list, capture_output=True)
    generate_scan_results_file(SCAN_RESULTS_FILE, port_scan)
    replace_file("temp.txt", SCAN_RESULTS_FILE)
    # LEFT OFF


def replace_file(fout, fin):

    with open(fin, "r") as original_file, open(fout, "w") as new_file:
        for line in original_file:
            processed_line = process_lines(line)
            new_file.write(processed_line)

            
            if os.path.exists(fout):
                os.remove(fin)
                os.rename(fout, fin)

















#top_port_scan_net_addr = nmap.scan_top_ports(str(network))