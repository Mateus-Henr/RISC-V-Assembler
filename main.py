import sys
from read_functions import *

"""main code"""

fileName = input("File name: ")

try:
    file = open(fileName, 'r')
except OSError:
    print("Error reading the file:", fileName)
    sys.exit()

with file:
    for line in file:
        if line not in ['\n', '\r\n']:
            print(build_instruction(line.strip()).to_machine_code())
