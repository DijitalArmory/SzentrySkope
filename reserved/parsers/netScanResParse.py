import re
import os
from data.line_signatures import (bad_signatures, semi_bad_signatures)




def process_lines(line):
    
    match = re.search(r"\d{1,5}/\w{3,4}\s+\S+\s{1,4}\S+", line)
    """
    Remove bad substrings and/or remove entire line if it contains a bad signature.
    """
    for substring in semi_bad_signatures:
        line = line.replace(substring, "")
    if any(signature in line for signature in bad_signatures):
        line = ""
        
    if match:
            print("Found match in line: ", line)
            line = re.sub(r"(\d{1,5}/\w{3,4})\s+(\S+\s{1,4}\S+)", r"\1 <--port\n\2 <-- state/protocol", line)

    return line

def replace_file(fout, fin):

    with open("original_file.txt", "r") as original_file, open("new_file.txt", "w") as new_file:
        for line in original_file:
            processed_line = process_lines(line)
            new_file.write(processed_line)

            
            if os.path.exists("new_file.txt"):
                os.remove("original_file.txt")
                os.rename("new_file.txt", "original_file.txt")