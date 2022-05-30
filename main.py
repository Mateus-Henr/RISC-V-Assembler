import sys
from converter import *

FILE_PATH = "test_files/"

"""main code"""

fileName = input("File name: ")

try:
    file = open(f"{FILE_PATH}{fileName}", 'r')
except OSError:
    print("Error reading the file:", fileName)
    sys.exit()

with file:
    for line in file:
        if line not in ['\n', '\r\n']:
            print(build_instruction(line.strip()).to_machine_code())
