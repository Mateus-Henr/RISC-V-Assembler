"""folder that store the converter functions, that stores the values in variables and convert the .asm in machine
code. """

# internal imports
from instruction_types import *

# global variables
FUNCT3 = 0
FUNCT7 = 1


# function to convert the instructions into objects of each type
def assemble_instruction(line: str):
    """receive a string line, from the archive, and separate each part os the instruction, finally convert it in an
    object of the detected type. Using the global functions of dictionaries and the get_register_binary_code to do the
    objects, also utilizes the global variables of Funct7 and Funct3 to take the values of the dictionary.

     input: a string that represents the line of the file.

     output: an object of the detected type in can be:

     Rtype object: funct7, rs2, rs1, funct3, rd.
     Itype object: immediate, rs1, funct3, rd.
     Stype object: immediate7, rs2, rs2, funct3, immediate5.
     Utype object: immediate, rd."""

    instruction_name = line.split()[0]

    # se if the function is a Rtype and split/replace the strings.
    if instruction_name in R_TYPES:
        user_input = line.replace(",", " ").split()

        # use the function that gets the registers binary code and the dictionary of the Rtype to create the binaries.
        instruction = {
            "funct7": R_TYPES[user_input[0]][FUNCT7],
            "rs2": get_register_binary_code(user_input[3]),
            "rs1": get_register_binary_code(user_input[2]),
            "funct3": R_TYPES[user_input[0]][FUNCT3],
            "rd": get_register_binary_code(user_input[1])
        }

        # return a Rtype unctions fild with the gated binaries.
        return RType(instruction["funct7"],
                     instruction["rs2"],
                     instruction["rs1"],
                     instruction["funct3"],
                     instruction["rd"]).to_machine_code()

    # se if the function is a Itype and split/replace the strings
    elif instruction_name in I_TYPES:
        user_input = line.replace(",", " ").split()

        # use the function that gets the registers binary/immediate code and the dictionary of the Itype to create
        # the binaries.
        instruction = {
            "immediate": get_immediate_binary_12bits(user_input[3]),
            "rs1": get_register_binary_code(user_input[2]),
            "funct3": I_TYPES[instruction_name][FUNCT3],
            "rd": get_register_binary_code(user_input[1])
        }

        # return a Itype unctions fild with the gated binaries.
        return IType(instruction["immediate"],
                     instruction["rs1"],
                     instruction["funct3"],
                     instruction["rd"]).to_machine_code()

    # se if the function is a Stype and split/replace the strings
    elif instruction_name in S_TYPES:
        user_input = line.replace(",", " ").replace("(", " ").replace(")", " ").split()

        # immediate variable that stores the output of the get_immediate_binary_12bits
        immediate = get_immediate_binary_12bits(user_input[2])

        # use the function that gets the registers/immediates binary code and the dictionary of the Stype to create
        # the binaries.
        instruction = {
            "immediate7": immediate[5:12],
            "rs2": get_register_binary_code(user_input[3]),
            "rs1": get_register_binary_code(user_input[1]),
            "funct3": S_TYPES[instruction_name][FUNCT3],
            "immediate5": immediate[0:5]
        }

        # return a Stype unctions fild with the gated binaries.
        return SType(instruction["immediate7"],
                     instruction["rs2"],
                     instruction["rs1"],
                     instruction["funct3"],
                     instruction["immediate5"]).to_machine_code()

    # se if the function is a Utype and split/replace the strings
    elif instruction_name in U_TYPES:
        user_input = line.replace(",", " ").replace("(", " ").replace(")", " ").split()

        # use the function that gets the registers/immediate binary code and the dictionary of the Stype to create
        # the binaries.
        instruction = {
            "immediate": get_immediate_binary_20bits(user_input[2]),
            "rd": get_register_binary_code(user_input[1])
        }

        # return a Stype unctions fild with the gated binaries.
        return UType(instruction["immediate"],
                     instruction["rd"]).to_machine_code()
    # print a message error if the instruction is not supported
    else:
        print(f"ERROR: Instruction name '{instruction_name}' not in the instruction set.")


# function that return the binary code of the register
def get_register_binary_code(register: str):
    """receives a string from the splited line and return a binary of the regular register.

    input: register string

    output: a 5 bits binary number."""
    return "{0:05b}".format(overflow_if_true_non_negative(convert_to_decimal(register.replace("x", "")), 5))


# function that return the binary code of the immediate
def get_immediate_binary_12bits(immediate: str):
    """receives a string from the splited line and return a binary of the regular immediate.

    input: immediate string

    output: a 12 bits binary number."""
    return "{0:012b}".format(overflow_if_true(convert_to_decimal(immediate), 11) & 0b111111111111)


# function that return the binary code of the 20bits immediate
def get_immediate_binary_20bits(immediate: str):
    """receives a string from the splited line and return a binary of the 20 bits immediate.

    input: immediate string

    output: a 20 bits binary number."""
    return "{0:020b}".format(overflow_if_true(convert_to_decimal(immediate), 19) & 0b11111111111111111111)


# function that performs the overflow
def overflow_if_true_non_negative(value: int, max_bits: int):
    """define a max value and return another if the overflow happens or not returning the rest if it happens

    input: a int value, a max value

    output: int max value or a value"""
    max_value = 2 ** max_bits

    return value % max_value if value >= max_value or value < 0 else value


def overflow_if_true(value: int, max_bits: int):
    min_value = -(2 ** max_bits)
    max_value = -min_value

    if value >= max_value:
        return value % max_value
    elif value <= min_value:
        return -(value % value)

    return value


def convert_to_decimal(value: str):
    try:
        if "0x" in value:
            return int(value, 16)
        elif all(letter == '0' or letter == '1' for letter in value):
            return int(value, 2)
        else:
            return int(value)
    except ValueError:
        print("ERROR: Syntax error, unexpected values. Setting invalid parameter to 0.")
        return 0
