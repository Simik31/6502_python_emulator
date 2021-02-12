# ######################################
#  Copyright (c) 2021                  #
#                                      #
#  Author: Martin Šimara               #
#  Last modified on 12.2.2021          #
# ######################################

"""
The 6502 microprocessor supports a 256 byte stack fixed between memory locations $0100 and $01FF.
A special 8-bit register, S, is used to keep track of the next free byte of stack space.
Pushing a byte on to the stack causes the value to be stored at the current free location (e.g. $0100,S)
and then the stack pointer is post decremented. Pull operations reverse this procedure.

The stack register can only be accessed by transferring its value to or from the X register.
Its value is automatically modified by push/pull instructions, subroutine calls and returns,
interrupts and returns from interrupts.
"""

from Instructions.Stack_Operations import PHA
from Instructions.Stack_Operations import PHP
from Instructions.Stack_Operations import PLA
from Instructions.Stack_Operations import PLP
from Instructions.Stack_Operations import TSX
from Instructions.Stack_Operations import TXS

Stack_Operations_Dictionary = {
    TSX.IMPLIED.OPCODE.get_hex_value(): TSX.IMPLIED.IMPLIED,

    TXS.IMPLIED.OPCODE.get_hex_value(): TXS.IMPLIED.IMPLIED,

    PHA.IMPLIED.OPCODE.get_hex_value(): PHA.IMPLIED.IMPLIED,

    PHP.IMPLIED.OPCODE.get_hex_value(): PHP.IMPLIED.IMPLIED,

    PLA.IMPLIED.OPCODE.get_hex_value(): PLA.IMPLIED.IMPLIED,

    PLP.IMPLIED.OPCODE.get_hex_value(): PLP.IMPLIED.IMPLIED,
}
