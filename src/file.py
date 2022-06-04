import converter
import os

# Default file paths so the user don't have to specify the folders;.
INPUT_FILE_PATH = f"{os.path.split(os.path.dirname(__file__))[-2]}/input_files/"
OUTPUT_FILE_PATH = f"{os.path.split(os.path.dirname(__file__))[-2]}/output_files/"


def read_file_and_generate_output(input_filename: str, output_filename: str):
    """
    Reads data from a file and writes it out in an output file.

    Parameters
    ----------
    input_filename : str
        name of the input file.
    output_filename : str
        name of the output file.
    """
    try:
        input_file = open(f"{INPUT_FILE_PATH}{input_filename}", "r")

        try:
            output_file = open(f"{OUTPUT_FILE_PATH}{output_filename}.bin", "w+")

            with output_file:
                with input_file:
                    for line in input_file:
                        if pre_check_line(line):
                            binary_value = converter.convert_instruction_to_binary(line)
                            if binary_value:
                                output_file.write(f"{binary_value}\n")

            print(f"Output file generated at: {OUTPUT_FILE_PATH}{output_filename}.bin.")

        except OSError:
            print(f"ERROR: Could not create output file: '{output_filename}.bin'.")

    except FileNotFoundError:
        print(f"ERROR: No such file or directory: '{input_filename}'.")


def read_file_and_print(input_filename: str):
    """
    Reads data from a file and prints out result on the console.

    Parameters
    ----------
    input_filename : str
        name of the input file.
    """

    try:
        input_file = open(f"{INPUT_FILE_PATH}{input_filename}", "r")

        with input_file:
            print(f"Translated instructions from '{input_filename}':")
            for line in input_file:
                if pre_check_line(line):
                    binary_value = converter.convert_instruction_to_binary(line)
                    if binary_value:
                        print(binary_value)
                    else:
                        print("Invalid instruction, jumping it.")

    except FileNotFoundError:
        print(f"ERROR: No such file or directory: '{input_filename}'.")


def pre_check_line(line_to_check: str):
    """
    Checks if a line is a comment or an empty line.

    Parameters
    ----------
    line_to_check : str
        line to check.

    Returns
    -------
    bool
        whether the line is not a comment or an empty line.
    """

    line_to_check = line_to_check.strip()
    return line_to_check not in ['\n', '\r\n'] and len(line_to_check) > 0 and line_to_check[0] != "#"
