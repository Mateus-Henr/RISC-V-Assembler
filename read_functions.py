"""Define different class for the types"""


#
class RType:
    """ """

    def __int__(self, funct7, rs2, rs1, funct3, rd, opcode):
        self.funct7 = funct7
        self.rs2 = rs2
        self.rs1 = rs1
        self.funct3 = funct3
        self.rd = rd
        self.opcode = opcode


#
class IType:
    """ """

    def __int__(self, immediate, rs1, funct3, rd, opcode):
        self.immediate = immediate
        self.rs1 = rs1
        self.funct3 = funct3
        self.rd = rd
        self.opcode = opcode


#
class SType:
    """ """

    def __int__(self, immediate7, rs2, rs1, funct3, immediate5, opcode):
        self.immediate7 = immediate7
        self.rs2 = rs2
        self.rs1 = rs1
        self.funct3 = funct3
        self.immediate5 = immediate5
        self.opcode = opcode


#
class UType:
    """ """
    def __int__(self, immediate, rd, opcode):
        self.immediate = immediate
        self.rd = rd
        self.opcode = opcode
