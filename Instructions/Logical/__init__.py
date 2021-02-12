# ######################################
#  Copyright (c) 2021                  #
#                                      #
#  Author: Martin Šimara               #
#  Last modified on 12.2.2021          #
# ######################################

"""
The following instructions perform logical operations on the contents of the accumulator and value held in memory.
The BIT instruction performs a logical AND to test the presence of bits in the memory value to set the flags
but does not keep the result.
"""

from Instructions.Logical import AND
from Instructions.Logical import BIT
from Instructions.Logical import EOR
from Instructions.Logical import ORA

Logical_Dictionary = {
    AND.INDIRECT_X.OPCODE.get_hex_value(): AND.INDIRECT_X.INDIRECT_X,
    AND.ZERO_PAGE.OPCODE.get_hex_value(): AND.ZERO_PAGE.ZERO_PAGE,
    AND.IMMEDIATE.OPCODE.get_hex_value(): AND.IMMEDIATE.IMMEDIATE,
    AND.ABSOLUTE.OPCODE.get_hex_value(): AND.ABSOLUTE.ABSOLUTE,
    AND.INDIRECT_Y.OPCODE.get_hex_value(): AND.INDIRECT_Y.INDIRECT_Y,
    AND.ZERO_PAGE_X.OPCODE.get_hex_value(): AND.ZERO_PAGE_X.ZERO_PAGE_X,
    AND.ABSOLUTE_Y.OPCODE.get_hex_value(): AND.ABSOLUTE_Y.ABSOLUTE_Y,
    AND.ABSOLUTE_X.OPCODE.get_hex_value(): AND.ABSOLUTE_X.ABSOLUTE_X,

    EOR.INDIRECT_X.OPCODE.get_hex_value(): EOR.INDIRECT_X.INDIRECT_X,
    EOR.ZERO_PAGE.OPCODE.get_hex_value(): EOR.ZERO_PAGE.ZERO_PAGE,
    EOR.IMMEDIATE.OPCODE.get_hex_value(): EOR.IMMEDIATE.IMMEDIATE,
    EOR.ABSOLUTE.OPCODE.get_hex_value(): EOR.ABSOLUTE.ABSOLUTE,
    EOR.INDIRECT_Y.OPCODE.get_hex_value(): EOR.INDIRECT_Y.INDIRECT_Y,
    EOR.ZERO_PAGE_X.OPCODE.get_hex_value(): EOR.ZERO_PAGE_X.ZERO_PAGE_X,
    EOR.ABSOLUTE_Y.OPCODE.get_hex_value(): EOR.ABSOLUTE_Y.ABSOLUTE_Y,
    EOR.ABSOLUTE_X.OPCODE.get_hex_value(): EOR.ABSOLUTE_X.ABSOLUTE_X,

    ORA.INDIRECT_X.OPCODE.get_hex_value(): ORA.INDIRECT_X.INDIRECT_X,
    ORA.ZERO_PAGE.OPCODE.get_hex_value(): ORA.ZERO_PAGE.ZERO_PAGE,
    ORA.IMMEDIATE.OPCODE.get_hex_value(): ORA.IMMEDIATE.IMMEDIATE,
    ORA.ABSOLUTE.OPCODE.get_hex_value(): ORA.ABSOLUTE.ABSOLUTE,
    ORA.INDIRECT_Y.OPCODE.get_hex_value(): ORA.INDIRECT_Y.INDIRECT_Y,
    ORA.ZERO_PAGE_X.OPCODE.get_hex_value(): ORA.ZERO_PAGE_X.ZERO_PAGE_X,
    ORA.ABSOLUTE_Y.OPCODE.get_hex_value(): ORA.ABSOLUTE_Y.ABSOLUTE_Y,
    ORA.ABSOLUTE_X.OPCODE.get_hex_value(): ORA.ABSOLUTE_X.ABSOLUTE_X,

    BIT.ZERO_PAGE.OPCODE.get_hex_value(): BIT.ZERO_PAGE.ZERO_PAGE,
    BIT.ABSOLUTE.OPCODE.get_hex_value(): BIT.ABSOLUTE.ABSOLUTE
}
