"""Define different class for the types"""


#
class RType(object):
    """ """

    def __init__(self, funct7: str, rs2: str, rs1: str, funct3: str, rd: str, opcode="0110011"):
        self.funct7 = funct7
        self.rs2 = rs2
        self.rs1 = rs1
        self.funct3 = funct3
        self.rd = rd
        self.opcode = opcode

    def to_machine_code(self):
        return f"{self.funct7} {self.rs2} {self.rs1} {self.funct3} {self.rd} {self.opcode}"


#
class IType(object):
    """ """

    def __init__(self, immediate: str, rs1: str, funct3: str, rd: str, opcode="0010011"):
        self.immediate = immediate
        self.rs1 = rs1
        self.funct3 = funct3
        self.rd = rd
        self.opcode = opcode

    def to_machine_code(self):
        return f"{self.immediate} {self.rs1} {self.funct3} {self.rd} {self.opcode}"


#
class SType(object):
    """ """

    def __init__(self, immediate7: str, rs2: str, rs1: str, funct3: str, immediate5: str, opcode="0100011"):
        self.immediate7 = immediate7
        self.rs2 = rs2
        self.rs1 = rs1
        self.funct3 = funct3
        self.immediate5 = immediate5
        self.opcode = opcode

    def to_machine_code(self):
        return f"{self.immediate7} {self.rs2} {self.rs1} {self.funct3} {self.immediate5} {self.opcode}"


#
class UType(object):
    """ """

    def __init__(self, immediate: str, rd: str, opcode="0110111"):
        self.immediate = immediate
        self.rd = rd
        self.opcode = opcode

    def to_machine_code(self):
        return f"{self.immediate} {self.rd} {self.opcode}"
