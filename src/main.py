"""Main code of the project, open the selected file and return the machine binary code of it."""

import sys
from file import *

if __name__ == "__main__":
    if len(sys.argv) == 2:
        read_file_and_print(sys.argv[1])
    elif len(sys.argv) == 6:
        if sys.argv[4] == "-o":
            read_file_and_generate_output(sys.argv[3], sys.argv[5])
        else:
            raise ValueError("ERROR: Missing arguments.")
    else:
        raise ValueError("ERROR: Missing arguments or too many arguments.")
