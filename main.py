"""main code"""

from read_functions import *

# FILE_PATH = "../"

FUNCT3 = 0
FUNCT7 = 1

fileName = str(input('File name: '))
# [a for a in dir(build_instruction(line)) if not a.startswith('__')
# tryes to read the archive, if it can't, it outputs an error message

with open(fileName, 'r') as file:
    for line in file:
        if line not in ['\n', '\r\n']:
            print(build_instruction(line.strip()).to_machine_code())
