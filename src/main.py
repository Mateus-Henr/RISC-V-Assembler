import sys
import file

FORMATS = "\nAccepted formats:" \
          "\nPyCharm:" \
          "\n• 'INPUT_FILENAME.asm'" \
          "\n• 'INPUT_FILENAME.asm -o OUTPUT_FILENAME'" \
          "\nCMD/Terminal: (in the project's root folder)" \
          "\n• 'python3 src/main.py INPUT_FILENAME.asm -o OUTPUT_FILENAME'" \
          "\n• 'python3 src/main.py INPUT_FILENAME.asm"

if __name__ == "__main__":
    args_length = len(sys.argv)
    if args_length == 2:
        file.read_file_and_print(sys.argv[1])
    elif args_length == 4 or args_length == 5:  # Pycharm, CMD or terminal.
        if sys.argv[2] == "-o":
            file.read_file_and_generate_output(sys.argv[1], sys.argv[3])
        else:
            raise ValueError(f"ERROR: Missing arguments.{FORMATS}")
    else:
        raise ValueError(f"ERROR: Missing argument(s) or too many arguments.{FORMATS}")
