from converter import *

FILE_PATH = "test_files/"

filename = input("Filename: ")

try:
    input_file = open(f"{FILE_PATH}{filename}", "r")
except FileNotFoundError:
    raise FileNotFoundError(f"Error reading the file:{filename}")

try:
    outputFile = open(f"{FILE_PATH}{filename.split('.')[0]}-output.ijvm", "w+")
except OSError:
    raise OSError("ERROR: Could not create the output file")


def pre_check_line(line_to_check: str):
    line_to_check = line_to_check.strip()
    return line_to_check not in ['\n', '\r\n'] and len(line_to_check) > 0 and line_to_check[0] != "#"


with outputFile:
    with input_file:
        for line in input_file:
            if pre_check_line(line):
                outputFile.write(f"{build_instruction(line.strip()).to_machine_code()}\n")


def get_filename_without_extension(filename_to_format: str):
    return filename_to_format.split(".") if "." in filename_to_format else filename_to_format
