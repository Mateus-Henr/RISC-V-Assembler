"""Main code of the project, open the selected file and return the machine binary code of it."""

import sys
from file import *

if __name__ == "__main__":
    if len(sys.argv) == 2:
        read_file_and_print(sys.argv[1])
    # When using PyCharm we can set in the parameters box only "input_file -o output_file" (i.e. "input.asm -o output")
    elif len(sys.argv) == 4 or len(sys.argv) == 5:
        if sys.argv[2] == "-o":
            read_file_and_generate_output(sys.argv[1], sys.argv[3])
        else:
            raise ValueError("ERROR: Missing arguments.")
    else:
        raise ValueError("ERROR: Missing arguments or too many arguments.")
