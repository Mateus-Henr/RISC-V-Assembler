# Array indexes.
FUNCT3 = 0
FUNCT7 = 1

# Instructions divided by their respective types.
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

    # Pseudo instruction
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


class RType(object):
    """
    A class used to represent an instruction of type R.

    ...

    Attributes
    ----------
    funct7 : str
        binary value of funct7.
    rs2 : str
        binary value of rs2.
    rs1 : str
        binary value of rs1.
    funct3 : str
        binary value of funct3.
    rd  : str
        binary value of rd.
    opcode : str
        binary value of opcode.

    Methods
    -------
    to_machine_code()
        Converts the class fields to a string that represents the binary code
        of the operation.
    """

    def __init__(self, funct7: str, rs2: str, rs1: str, funct3: str, rd: str, opcode="0110011"):
        self.funct7 = funct7
        self.rs2 = rs2
        self.rs1 = rs1
        self.funct3 = funct3
        self.rd = rd
        self.opcode = opcode

    def to_machine_code(self):
        """
        Converts fields to a string in a certain order.
        """

        return f"{self.funct7}{self.rs2}{self.rs1}{self.funct3}{self.rd}{self.opcode}"


class IType(object):
    """
    A class used to represent an instruction of type I.

    ...

    Attributes
    ----------
    immediate : str
        binary value of immediate.
    rs1 : str
        binary value of rs1.
    funct3 : str
        binary value of funct3.
    rd  : str
        binary value of rd.
    opcode : str
        binary value of opcode.

    Methods
    -------
    to_machine_code()
        Converts the class fields to a string that represents the binary code
        of the operation.
    """

    def __init__(self, immediate: str, rs1: str, funct3: str, rd: str, opcode="0010011"):
        self.immediate = immediate
        self.rs1 = rs1
        self.funct3 = funct3
        self.rd = rd
        self.opcode = opcode

    # function that transforms the class in a machine code
    def to_machine_code(self):
        """
        Converts fields to a string in a certain order.
        """

        return f"{self.immediate}{self.rs1}{self.funct3}{self.rd}{self.opcode}"


class SType(object):
    """
    A class used to represent an instruction of type S.

    ...

    Attributes
    ----------
    immediate7 : str
        binary value within range of 5 to 12.
    rs2 : str
        binary value of rs2.
    rs1 : str
        binary value of rs1.
    funct3 : str
        binary value of funct3.
    immediate5 : str
        binary value within range of 0 to 5.
    opcode : str
        binary value of opcode.

    Methods
    -------
    to_machine_code()
        Converts the class fields to a string that represents the binary code
        of the operation.
    """

    def __init__(self, immediate7: str, rs2: str, rs1: str, funct3: str, immediate5: str, opcode="0100011"):
        self.immediate7 = immediate7
        self.rs2 = rs2
        self.rs1 = rs1
        self.funct3 = funct3
        self.immediate5 = immediate5
        self.opcode = opcode

    def to_machine_code(self):
        """
        Converts fields to a string in a certain order.
        """

        return f"{self.immediate7}{self.rs2}{self.rs1}{self.funct3}{self.immediate5}{self.opcode}"


# a Utype object to store the instruction's values
class UType(object):
    """
    A class used to represent an instruction of type U.

    ...

    Attributes
    ----------
    immediate : str
        binary value of immediate.
    rd  : str
        binary value of rd.
    opcode : str
        binary value of opcode.

    Methods
    -------
    to_machine_code()
        Converts the class fields to a string that represents the binary code
        of the operation.
    """

    def __init__(self, immediate: str, rd: str, opcode="0110111"):
        self.immediate = immediate
        self.rd = rd
        self.opcode = opcode

    def to_machine_language(self):
        """
        Converts fields to a string in a certain order.
        """

        return f"{self.immediate}{self.rd}{self.opcode}"
