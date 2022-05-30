"""Define different class for the types:

     Rtype object: funct7, rs2, rs1, funct3, rd.
     Itype object: immediate, rs1, funct3, rd.
     Stype object: immediate7, rs2, rs2, funct3, immediate5.
     Utype object: immediate, rd.

     and for each of then a function that convert the class to a string"""


# a Rtype object to store the instruction's values
class RType(object):
    """store the values of the Rtype, and the function that transforms it in a string machine code.

        stored values: funct7, rs2, rs1, funct3, rd and opcode(0110011).
        (all the stored values are strings)"""

    def __init__(self, funct7: str, rs2: str, rs1: str, funct3: str, rd: str, opcode="0110011"):
        self.funct7 = funct7
        self.rs2 = rs2
        self.rs1 = rs1
        self.funct3 = funct3
        self.rd = rd
        self.opcode = opcode

    # function that transforms the class in a machine code
    def to_machine_code(self):
        """transform the class in a machine code.
        input: Rtype class(self)
        output: a machine code string"""
        return f"{self.funct7} {self.rs2} {self.rs1} {self.funct3} {self.rd} {self.opcode}"


# a Itype object to store the instruction's values
class IType(object):
    """store the values of the Itype, and the function that transforms it in a string machine code.

        stored values: immediate, rs1, funct3, rd, opcode(0010011).
        (all the stored values are strings)"""

    def __init__(self, immediate: str, rs1: str, funct3: str, rd: str, opcode="0010011"):
        self.immediate = immediate
        self.rs1 = rs1
        self.funct3 = funct3
        self.rd = rd
        self.opcode = opcode

    # function that transforms the class in a machine code
    def to_machine_code(self):
        """transform the class in a machine code.
        input: Itype class(self)
        output: a machine code string"""

        return f"{self.immediate} {self.rs1} {self.funct3} {self.rd} {self.opcode}"


# a Stype object to store the instruction's values
class SType(object):
    """store the values of the Stype, and the function that transforms it in a string machine code.

        stored values: immediate7, rs2, rs2, funct3, immediate5, opcode(0100011).
        (all the stored values are strings)"""

    def __init__(self, immediate7: str, rs2: str, rs1: str, funct3: str, immediate5: str, opcode="0100011"):
        self.immediate7 = immediate7
        self.rs2 = rs2
        self.rs1 = rs1
        self.funct3 = funct3
        self.immediate5 = immediate5
        self.opcode = opcode

    # function that transforms the class in a machine code
    def to_machine_code(self):
        """transform the class in a machine code.
        input: Stype class(self)
        output: a machine code string"""

        return f"{self.immediate7} {self.rs2} {self.rs1} {self.funct3} {self.immediate5} {self.opcode}"


# a Utype object to store the instruction's values
class UType(object):
    """store the values of the Utype, and the function that transforms it in a string machine code.

        stored values: immediate, rd, opcode(0110111).
        (all the stored values are strings)"""

    def __init__(self, immediate: str, rd: str, opcode="0110111"):
        self.immediate = immediate
        self.rd = rd
        self.opcode = opcode

    # function that transforms the class in a machine code
    def to_machine_code(self):
        """transform the class in a machine code.
        input: Utype class(self)
        output: a machine code string"""

        return f"{self.immediate} {self.rd} {self.opcode}"
