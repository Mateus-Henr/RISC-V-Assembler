from instruction_types import RType, IType, SType, UType

FUNCT3 = 0
FUNCT7 = 1

R_TYPES = {
    "add": ["000", "0000000"],
    "sub": ["000", "0100000"],
    "and": ["111", "0000000"],
    "or": ["110", "0000000"],
    "xor": ["100", "0000000"],
    "sll": ["001", "0000000"],
    "srl": ["101", "0000000"],
    "lrd": ["011", "0010000"],
    "scd": ["011", "0001100"],

    # Pseudo instructions
    "neg": ["000", "0100000"]
}

I_TYPES = {
    "addi": ["000"],
    "andi": ["111"],
    "ori": ["110"],
    "lb": ["000"],
    "lbu": ["100"],
    "lh": ["001"],
    "lhu": ["101"],
    "lw": ["010"],
    "lwu": ["110"],
    "ld": ["011"],

    # Pseudo instructions
    "nop": ["000"],
    "li": ["000"],
    "mv": ["000"]
}

S_TYPES = {
    "sd": ["111"],
    "sw": ["010"],
    "sh": ["001"],
    "sb": ["000"]
}

U_TYPES = {"lui"}


def build_instruction(line: str):
    """"""

    instruction_name = line.split()[0]

    if instruction_name in R_TYPES:
        user_input = line.replace(",", " ").split()

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
                     instruction["rd"])

    elif instruction_name in I_TYPES:
        user_input = line.replace(",", " ").split()

        instruction = {
            "immediate": get_immediate_binary_12bits(user_input[3]),
            "rs1": get_register_binary_code(user_input[2]),
            "funct3": get_register_binary_code(user_input[1]),
            "rd": I_TYPES[instruction_name][FUNCT3]
        }

        return IType(instruction["immediate"],
                     instruction["rs1"],
                     instruction["funct3"],
                     instruction["rd"])

    elif instruction_name in S_TYPES:
        user_input = line.replace(",", " ").replace("(", " ").replace(")", " ").split()

        immediate = get_immediate_binary_12bits(user_input[2])

        instruction = {
            "immediate7": immediate[5:11],
            "rs2": get_register_binary_code(user_input[3]),
            "rs1": get_register_binary_code(user_input[1]),
            "funct3": S_TYPES[instruction_name][FUNCT3],
            "immediate5": immediate[0:4]
        }

        return SType(instruction["immediate7"],
                     instruction["rs2"],
                     instruction["rs1"],
                     instruction["funct3"],
                     instruction["immediate5"])

    elif instruction_name in U_TYPES:
        user_input = line.replace(",", " ").replace("(", " ").replace(")", " ").split()

        instruction = {
            "immediate": get_immediate_binary_20bits(user_input[2]),
            "rd": get_register_binary_code(user_input[1])
        }

        return UType(instruction["immediate"],
                     instruction["rd"])

    else:
        print(f"ERROR: Instruction name '{instruction_name}' not in the instruction set.")


def get_register_binary_code(register):
    return "{0:05b}".format(perform_overflow_if_happens(int(register.replace("x", "")), 5))


def get_immediate_binary_12bits(immediate):
    return "{0:012b}".format(perform_overflow_if_happens(int(immediate), 12))


def get_immediate_binary_20bits(immediate):
    return "{0:020b}".format(perform_overflow_if_happens(int(immediate), 20))


def perform_overflow_if_happens(value, max_bits):
    max_value = 2 ** max_bits
    return value % max_value if value >= max_value else value
