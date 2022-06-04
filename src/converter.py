from instruction_types import *


def convert_instruction_to_binary(line: str):
    """
    Converts an instruction to binary code if valid.

    Parameters
    ----------
    line : str
        A string that contains the instruction.

    Returns
    -------
    str
        A string containing the binary code of the translated instruction if valid, or
        an empty string if invalid.
    """

    instruction_name = line.split()[0]

    if instruction_name in R_TYPES:
        user_input = line.replace(",", " ").split()[:4]

        if check_invalid_values(user_input):
            return ""

        # Created to make readability easier when passing values to the object type.
        instruction = {
            "funct7": R_TYPES[user_input[0]][FUNCT7],
            "rs2": get_register_binary_code(user_input[3]),
            "rs1": get_register_binary_code(user_input[2]),
            "funct3": R_TYPES[user_input[0]][FUNCT3],
            "rd": get_register_binary_code(user_input[1])
        }

        return RType(instruction["funct7"],
                     instruction["rs2"],
                     instruction["rs1"],
                     instruction["funct3"],
                     instruction["rd"]).to_machine_code()

    elif instruction_name in I_TYPES:
        user_input = line.replace(",", " ").split()[:4]

        if check_invalid_values(user_input):
            return ""

        # Created to make readability easier when passing values to the object type.
        instruction = {
            "immediate": get_immediate_binary_12bits(user_input[3]),
            "rs1": get_register_binary_code(user_input[2]),
            "funct3": I_TYPES[instruction_name][FUNCT3],
            "rd": get_register_binary_code(user_input[1])
        }

        return IType(instruction["immediate"],
                     instruction["rs1"],
                     instruction["funct3"],
                     instruction["rd"]).to_machine_code()

    elif instruction_name in S_TYPES:
        user_input = line.replace(",", " ").replace("(", " ").replace(")", " ").split()[:4]

        if check_invalid_values(user_input):
            return ""

        immediate = get_immediate_binary_12bits(user_input[2])

        # Created to make readability easier when passing values to the object type.
        instruction = {
            "immediate7": immediate[5:12],
            "rs2": get_register_binary_code(user_input[3]),
            "rs1": get_register_binary_code(user_input[1]),
            "funct3": S_TYPES[instruction_name][FUNCT3],
            "immediate5": immediate[0:5]
        }

        return SType(instruction["immediate7"],
                     instruction["rs2"],
                     instruction["rs1"],
                     instruction["funct3"],
                     instruction["immediate5"]).to_machine_code()

    elif instruction_name in U_TYPES:
        user_input = line.replace(",", " ").replace("(", " ").replace(")", " ").split()[:3]

        if check_invalid_values(user_input):
            return ""

        # Created to make readability easier when passing values to the object type.
        instruction = {
            "immediate": get_immediate_binary_20bits(user_input[2]),
            "rd": get_register_binary_code(user_input[1])
        }

        return UType(instruction["immediate"],
                     instruction["rd"]).to_machine_language()

    # Prints a message if the instruction is not supported.
    print(f"ERROR: Instruction name '{instruction_name}' not in the instruction set.")
    return ""


# function that return the binary code of the register
def get_register_binary_code(register: str):
    """
    Converts a register to its binary number of 5-bits size.

    Parameters
    ----------
    register : str
        A string that containing the register.

    Returns
    -------
    str
        5-bits binary code of the register.
    """

    return "{0:05b}".format(
        overflow_if_true(convert_immediate_to_decimal(register.replace("x", "").replace("-", "")), 5))


def get_immediate_binary_12bits(immediate: str):
    """
    Converts an immediate its binary number of 12-bits size.

    Parameters
    ----------
    immediate : str
        A string containing the immediate.

    Returns
    -------
    str
        12-bits binary number of the immediate.
    """

    # The binary operation performed is for negative numbers.
    return "{0:012b}".format(
        overflow_or_underflow_if_true(convert_immediate_to_decimal(immediate), 11) & 0b111111111111)


# function that return the binary code of the 20bits immediate
def get_immediate_binary_20bits(immediate: str):
    """
    Converts an immediate its binary number of 20-bits size.

    Parameters
    ----------
    immediate : str
        A string containing the immediate.

    Returns
    -------
    str
        20-bits binary number of the immediate.
    """

    # The binary operation performed is for negative numbers.
    return "{0:020b}".format(
        overflow_or_underflow_if_true(convert_immediate_to_decimal(immediate), 19) & 0b11111111111111111111)


# function that performs the overflow
def overflow_if_true(value: int, max_bits: int):
    """
    Checks if value overflowed, if true it performs te overflow operation.

    Parameters
    ----------
    value : int
        The value to be checked.
    max_bits : int
        The maximum number of bits of the binary number.

    Returns
    -------
    int
       the same value passed in if it didn't overflow, otherwise the value after
       performing the overflow.
    """

    max_value = 2 ** max_bits

    return value % max_value if value >= max_value or value < 0 else value


def overflow_or_underflow_if_true(value: int, max_bits: int):
    """
    Checks if value overflowed or underflow-ed, if true it performs the overflow
    or underflow operation.

    Parameters
    ----------
    value : int
        The value to be checked.
    max_bits : int
        The maximum number of bits of the binary number.

    Returns
    -------
    int
        the same value passed in if it didn't overflow, otherwise the value after
        performing the overflow.
    """

    min_value = -(2 ** max_bits)
    max_value = -min_value

    if value >= max_value:
        return value % max_value
    elif value <= min_value:
        return -(value % value)

    return value


def convert_immediate_to_decimal(number: str):
    """
    Converts string to decimal (immediate), it supports the following number bases:
    - Binary
    - Hexadecimal
    - Decimal

    Parameters
    ----------
    number : str
        Number to be converted.

    Returns
    -------
    int
        decimal number if the passed in number is valid, otherwise, 0 is returned.
        When its invalid is because a register was passed in.
    """

    try:
        if "0x" in number:
            return int(number, 16)
        elif all(digit == '0' or digit == '1' for digit in number):
            return int(number, 2)
        return int(number)

    # This error is thrown if a register is passed in instead of an immediate.
    except ValueError:
        print("ERROR: Immediate expected, instead receiver was received. Setting invalid parameter to 0.")
        return 0


def check_invalid_values(items: list):
    """
    Checks if instruction parameters are valid.

    Parameters
    ----------
    items : list
        instruction's parameters.

    Returns
    -------
    bool
        whether the parameters are valid or not.
    """

    whitelist = ["x", "-"]

    for item_number in range(1, len(items)):
        for char in items[item_number]:
            if not char.isdigit() and char not in whitelist:
                return True

    return False
