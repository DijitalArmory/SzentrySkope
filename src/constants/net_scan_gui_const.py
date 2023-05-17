# Scan Techniques
sS = "TCP SYN"
sT = "TCP CON"
sA = "TCP SYN ACK"
sW = "TCP Window"
sM = "TCP Maimon"
sU = "UDP"
sN = "TCP NULL"
sF = "TCP FIN"
sX = "TCP XMAS"
sI = "Zombie"
sY = "SCTP INIT"
sZ = "COOKIE-ECHO"
b = "FTP Bounce"

scan_techniques_txt = [
    sS, sT, sA, sW, sM, sU, sN, sF, sX, sI, sY, sZ, b
]

# Port Range UI
PRANGE_1 = "PortX"
PRANGE_2 = "Service"
PRANGE_3 = "Vulns"

# SERVICE/VERSION DETECTION
sV = "Service Detection"

# Scan Intensity Constants
SCAN_1_INT = "Stealth"
SCAN_2_INT = "Aggression"
SCAN_3_INT = "Evasion"