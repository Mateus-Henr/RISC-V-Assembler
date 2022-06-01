"""Main code of the project, open the selected file and return the machine binary code of it."""

# internal imports
from converter import *

# stores the path file of the tests
INPUT_FILE_PATH = "input_files/"
OUTPUT_FILE_PATH = "output_files/"

# ask witch test inside the path file to run
filename = input("Filename: ")

# try to open the input file if it exists else returns an error message
try:
    input_file = open(f"{INPUT_FILE_PATH}{filename}", "r")
except FileNotFoundError:
    raise FileNotFoundError(f"Error reading the file:{filename}")

# try to create the output file if it can't return error message
try:
    output_file = open(f"{OUTPUT_FILE_PATH}{filename.split('.')[0]}-output.bin", "w+")
except OSError:
    raise OSError("ERROR: Could not create the output file")


# function that check if the line is readable and is not a comment line or an empty line
def pre_check_line(line_to_check: str):
    """receive a line to check if the line is readable, strip the line a check for empty spaces or comments.

    input: a line string to check.

    output: a string that is readable."""

    line_to_check = line_to_check.strip()
    return line_to_check not in ['\n', '\r\n'] and len(line_to_check) > 0 and line_to_check[0] != "#"

    # read each input file and use the build instruction to create a binary code for each instruction, and store it in the
    # output file


with output_file:
    with input_file:
        for line in input_file:
            if pre_check_line(line):
                output_file.write(f"{assemble_instruction(line)}\n")


# function that gets the file name without extension
def get_filename_without_extension(filename_to_format: str):
    """check is an . in the file that indicates an extension and return a string without it.

    input: a string with the file name
    output: a string with the file name without extension"""

    return filename_to_format.split(".") if "." in filename_to_format else filename_to_format
