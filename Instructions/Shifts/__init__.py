# ##############################
#  Copyright (c) 2021          #
#                              #
#  Author: Martin Šimara       #
#  Last modified on 12.2.2021  #
# ##############################

"""
Shift instructions cause the bits within either a memory location or the accumulator to be shifted by one bit position.
The rotate instructions use the contents if the carry flag (C) to fill the vacant position generated by the shift
and to catch the overflowing bit.
The arithmetic and logical shifts shift in an appropriate 0 or 1 bit as appropriate
but catch the overflow bit in the carry flag (C).
"""

from Instructions.Shifts import ASL
from Instructions.Shifts import LSR

Shifts_Dictionary = {
    ASL.ZERO_PAGE.OPCODE.get_hex_value(): ASL.ZERO_PAGE.ZERO_PAGE,
    ASL.ACCUMULATOR.OPCODE.get_hex_value(): ASL.ACCUMULATOR.ACCUMULATOR,
    ASL.ABSOLUTE.OPCODE.get_hex_value(): ASL.ABSOLUTE.ABSOLUTE,
    ASL.ZERO_PAGE_X.OPCODE.get_hex_value(): ASL.ZERO_PAGE_X.ZERO_PAGE_X,
    ASL.ABSOLUTE_X.OPCODE.get_hex_value(): ASL.ABSOLUTE_X.ABSOLUTE_X,

    LSR.ZERO_PAGE.OPCODE.get_hex_value(): LSR.ZERO_PAGE.ZERO_PAGE,
    LSR.ACCUMULATOR.OPCODE.get_hex_value(): LSR.ACCUMULATOR.ACCUMULATOR,
    LSR.ABSOLUTE.OPCODE.get_hex_value(): LSR.ABSOLUTE.ABSOLUTE,
    LSR.ZERO_PAGE_X.OPCODE.get_hex_value(): LSR.ZERO_PAGE_X.ZERO_PAGE_X,
    LSR.ABSOLUTE_X.OPCODE.get_hex_value(): LSR.ABSOLUTE_X.ABSOLUTE_X
}

