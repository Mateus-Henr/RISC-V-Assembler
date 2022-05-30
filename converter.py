from types import RType, IType, SType, UType

FUNCT3 = 0
FUNCT7 = 1


def build_instruction(line: str):
    """"""

    r_types = {
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

    i_types = {
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

    s_types = {
        "sd": ["111"],
        "sw": ["010"],
        "sh": ["001"],
        "sb": ["000"]
    }

    u_types = {"lui"}

    instruction = line.replace(",", " ").replace("(", " ").replace("-", " ").replace(")", " ").split()
    instruction_name = instruction[0]

    if instruction_name in r_types:
        return RType(r_types[instruction_name][FUNCT7],
                     get_register_binary_code(instruction[3]),
                     get_register_binary_code(instruction[2]),
                     r_types[instruction_name][FUNCT3],
                     get_register_binary_code(instruction[1]))

    elif instruction_name in i_types:
        return IType(get_immediate_binary_12bits(instruction[3]),
                     get_register_binary_code(instruction[2]),
                     get_register_binary_code(instruction[1]),
                     i_types[instruction_name][FUNCT3])

    elif instruction_name in s_types:
        immediate = get_immediate_binary_12bits(instruction[2])

        return SType(immediate[5:11],
                     get_register_binary_code(instruction[3]),
                     get_register_binary_code(instruction[1]),
                     s_types[instruction_name][FUNCT3],
                     immediate[0:4])

    elif instruction_name in u_types:
        return UType(get_immediate_binary_20bits(instruction[2]),
                     get_register_binary_code(instruction[1]))

    else:
        print(f"ERROR: Instruction name '{instruction_name}' not in the instruction set.")


def get_register_binary_code(register):
    return "{0:05b}".format(int(register.replace("x", "")))


def get_immediate_binary_12bits(immediate):
    return "{0:012b}".format(int(immediate))


def get_immediate_binary_20bits(immediate):
    return "{0:020b}".format(int(immediate))
