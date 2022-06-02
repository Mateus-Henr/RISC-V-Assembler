from converter import *
import os

INPUT_FILE_PATH = f"{os.path.split(os.path.dirname(__file__))[-2]}/input_files/"
OUTPUT_FILE_PATH = f"{os.path.split(os.path.dirname(__file__))[-2]}/output_files/"


def read_file_and_generate_output(input_filename: str, output_filename: str):
    try:
        input_file = open(f"{INPUT_FILE_PATH}{input_filename}", "r")

        try:
            output_file = open(f"{OUTPUT_FILE_PATH}{output_filename}.bin", "w+")

            with output_file:
                with input_file:
                    for line in input_file:
                        if pre_check_line(line):
                            output_file.write(f"{assemble_instruction(line)}\n")
            print(f"Output file generated at: {OUTPUT_FILE_PATH}{output_filename}.bin.")

        except OSError:
            print(f"ERROR: Could not create output file: '{output_filename}.bin'.")
    except FileNotFoundError:
        print(f"ERROR: No such file or directory: '{input_filename}'.")


def read_file_and_print(input_filename: str):
    try:
        input_file = open(f"{INPUT_FILE_PATH}{input_filename}", "r")

        with input_file:
            for line in input_file:
                if pre_check_line(line):
                    print(f"{assemble_instruction(line)}")
    except FileNotFoundError:
        print(f"ERROR: No such file or directory: '{input_filename}'.")


# function that check if the line is readable and is not a comment line or an empty line
def pre_check_line(line_to_check: str):
    """receive a line to check if the line is readable, strip the line a check for empty spaces or comments.

    input: a line string to check.

    output: a string that is readable."""

    line_to_check = line_to_check.strip()
    return line_to_check not in ['\n', '\r\n'] and len(line_to_check) > 0 and line_to_check[0] != "#"
