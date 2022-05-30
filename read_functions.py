"""Define different class for the types"""


#
class RType(object):
    """ """

    def __init__(self, funct7: str, rs2: str, rs1: str, funct3: str, rd: str, opcode='0110011'):
        self.funct7 = funct7
        self.rs2 = rs2
        self.rs1 = rs1
        self.funct3 = funct3
        self.rd = rd
        self.opcode = opcode

    def to_machine_code(self):
        return str(self.funct7 + self.rs2 + self.rs1 + self.funct3 + self.rd + self.opcode)


#
class IType(object):
    """ """

    def __init__(self, immediate: str, rs1: str, funct3: str, rd: str, opcode='0010011'):
        self.immediate = immediate
        self.rs1 = rs1
        self.funct3 = funct3
        self.rd = rd
        self.opcode = opcode

    def to_machine_code(self):
        return str(self.immediate + self.rs1 + self.funct3 + self.rd + self.opcode)


#
class SType(object):
    """ """

    def __init__(self, immediate7: str, rs2: str, rs1: str, funct3: str, immediate5: str, opcode='0100011'):
        self.immediate7 = immediate7
        self.rs2 = rs2
        self.rs1 = rs1
        self.funct3 = funct3
        self.immediate5 = immediate5
        self.opcode = opcode

    def to_machine_code(self):
        return str(self.immediate7 + self.rs2 + self.rs1 + self.funct3 + self.immediate5 + self.opcode)


#
class UType(object):
    """ """

    def __init__(self, immediate: str, rd: str, opcode='0110111'):
        self.immediate = immediate
        self.rd = rd
        self.opcode = opcode

    def to_machine_code(self):
        return str(self.immediate + self.rd + self.opcode)


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
        "scd": ["011", "0001100"]
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
        "ld": ["011"]
    }

    s_types = {
        "sd": ["111"],
        "sw": ["010"],
        "sh": ["001"],
        "sb": ["000"]
    }

    u_types = {"lui"}

    instruction = line.replace(",", " ").split()
    instruction_name = instruction[0]

    if instruction_name in r_types:
        return RType(r_types[instruction_name][FUNCT7],
                     get_register_binary_code(instruction[3]),
                     get_register_binary_code(instruction[2]),
                     r_types[instruction_name][FUNCT3],
                     get_register_binary_code(instruction[1]))

    if instruction_name in i_types:
        return IType(get_immediate_binary(int(instruction[3])),
                     get_register_binary_code(instruction[2]),
                     get_register_binary_code(instruction[1]),
                     i_types[instruction_name][FUNCT3])

    if instruction_name in s_types:
        immediate = get_immediate_binary(int(instruction[3]))

        return SType(immediate[7:11],
                     get_register_binary_code(instruction[3]),
                     get_register_binary_code(instruction[2]),
                     s_types[instruction_name][FUNCT3],
                     immediate[0:6])

    if instruction_name in u_types:
        return UType(get_immediate_binary(int(instruction[2])),
                     get_register_binary_code(instruction[1]))


def get_register_binary_code(register):
    return "{0:05b}".format(int(register.replace("x", "")))


def get_immediate_binary(immediate):
    return "{0:12b}".format(immediate)
