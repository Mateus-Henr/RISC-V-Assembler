import sys
from file import *

if __name__ == "__main__":
    args_length = len(sys.argv)
    if args_length == 2:
        read_file_and_print(sys.argv[1])
    elif args_length == 4 or args_length == 5:
        if sys.argv[2] == "-o":
            read_file_and_generate_output(sys.argv[1], sys.argv[3])
        else:
            raise ValueError("ERROR: Missing arguments.")
    else:
        raise ValueError("ERROR: Missing argument(s) or too many arguments.")
