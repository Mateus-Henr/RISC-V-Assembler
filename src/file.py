from converter import *

INPUT_FILE_PATH = "../input_files/"
OUTPUT_FILE_PATH = "output_files/"


def read_file_and_generate_output(input_file_path: str, output_file_path: str):
    try:
        input_file = open(input_file_path, "r")

        try:
            output_file = open(f"{input_file_path}.bin", "w+")

            with output_file:
                with input_file:
                    for line in input_file:
                        if pre_check_line(line):
                            output_file.write(f"{assemble_instruction(line)}\n")
            print(f"Output file generated at: {output_file_path}.bin")

        except OSError:
            raise OSError(f"ERROR: Could not create output file: '{output_file_path}.bin'.")
    except FileNotFoundError:
        raise FileNotFoundError(f"ERROR: No such file or directory: '{input_file_path}'.")


def read_file_and_print(input_file_path: str):
    try:
        input_file = open(input_file_path, "r")

        with input_file:
            for line in input_file:
                if pre_check_line(line):
                    print(f"{assemble_instruction(line)}")
    except FileNotFoundError:
        raise FileNotFoundError(f"ERROR: No such file or directory: '{input_file_path}'.")


# function that check if the line is readable and is not a comment line or an empty line
def pre_check_line(line_to_check: str):
    """receive a line to check if the line is readable, strip the line a check for empty spaces or comments.

    input: a line string to check.

    output: a string that is readable."""

    line_to_check = line_to_check.strip()
    return line_to_check not in ['\n', '\r\n'] and len(line_to_check) > 0 and line_to_check[0] != "#"
