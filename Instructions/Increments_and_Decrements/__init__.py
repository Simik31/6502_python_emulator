# ##############################
#  Copyright (c) 2021          #
#                              #
#  Author: Martin Šimara       #
#  Last modified on 12.2.2021  #
# ##############################

"""
Increment or decrement a memory location or one of the X or Y registers by one
setting the negative (N) and zero (Z) flags as appropriate
"""

from Instructions.Increments_and_Decrements import DEC
from Instructions.Increments_and_Decrements import DEX
from Instructions.Increments_and_Decrements import DEY
from Instructions.Increments_and_Decrements import INC
from Instructions.Increments_and_Decrements import INX
from Instructions.Increments_and_Decrements import INY

Increments_and_Decrements_Dictionary = {
    INC.ZERO_PAGE.OPCODE.get_hex_value(): INC.ZERO_PAGE.ZERO_PAGE,
    INC.ABSOLUTE.OPCODE.get_hex_value(): INC.ABSOLUTE.ABSOLUTE,
    INC.ZERO_PAGE_X.OPCODE.get_hex_value(): INC.ZERO_PAGE_X.ZERO_PAGE_X,
    INC.ABSOLUTE_X.OPCODE.get_hex_value(): INC.ABSOLUTE_X.ABSOLUTE_X,

    INX.IMPLIED.OPCODE.get_hex_value(): INX.IMPLIED.IMPLIED,

    INY.IMPLIED.OPCODE.get_hex_value(): INY.IMPLIED.IMPLIED,

    DEC.ZERO_PAGE.OPCODE.get_hex_value(): DEC.ZERO_PAGE.ZERO_PAGE,
    DEC.ABSOLUTE.OPCODE.get_hex_value(): DEC.ABSOLUTE.ABSOLUTE,
    DEC.ZERO_PAGE_X.OPCODE.get_hex_value(): DEC.ZERO_PAGE_X.ZERO_PAGE_X,
    DEC.ABSOLUTE_X.OPCODE.get_hex_value(): DEC.ABSOLUTE_X.ABSOLUTE_X,

    DEX.IMPLIED.OPCODE.get_hex_value(): DEX.IMPLIED.IMPLIED,

    DEY.IMPLIED.OPCODE.get_hex_value(): DEY.IMPLIED.IMPLIED
}
