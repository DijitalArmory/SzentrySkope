scan_init = "nmap"

udp_protocols = {
    "UDP" : "-sU"
}

scan_techniques = {
    "TCP SYN - Techinique"          : "-sS", 
    "TCP CON - Techinique"          : "-sT", 
    "TCP SYN ACK - Techinique"      : "-sA",
    "TCP Window - Techinique"       : "-sW",
    "TCP Maimon - Techinique"       :  "-sM", 
    "TCP NULL - Techinique"         : "-sN", 
    "TCP FIN - Techinique"          :  "-sF", 
    "TCP XMAS - Techinique"         : "-sX", 
    "Zombie - Techinique"           : "-sI",  
    "SCTP INIT - Techinique"        : "-sY",  
    "COOKIE-ECHO - Techinique"      : "-sZ", 
    "FTP Bounce - Techinique"       : "-b",
    "Consecutive ports - Port Spec" : "-r",
    "Ping Scan - Host"              : "-sn",
    "All Hosts Online"              : "-Pn",
    "TCP SYN - Host"                : "-PS",
    "ACK - Host"                    : "-PA",
    "UDP Discovery - Host"          : "-PU",
    "SCTP Discovery - Host"         : "-PY",
    "ICMP echo - Host"              : "-PE",
    "Timestamp - Host"              : "-PP",
    "netmask request - Host"        : "-PM",
    "No DNS Resolve - Host"         : "-n",
    "DNS Resolve - Host"            : "-R"
}

scan_service_detection = {
    "Service Detection"             : "-sV", 
    "Operating System Detection"    : "-O",
    "Service and OS Detection"      : "-A"
}


scan_scripts = {
    "script="                       : "-sC", 
    "script_trace"                  : "--script-trace",
    "script_db_update"              : "--script-updatedb"
}

scan_technique_options_gui = list(scan_techniques.keys())

scan_technique_options = list(scan_techniques.values())