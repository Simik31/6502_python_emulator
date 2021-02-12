# ######################################
#  Copyright (c) 2021                  #
#                                      #
#  Author: Martin Šimara               #
#  Last modified on 12.2.2021          #
# ######################################

"""
These instructions transfer a single byte between memory and one of the registers.
Load operations set the negative (N) and zero (Z) flags depending on the value of transferred.
Store operations do not affect the flag settings.
"""

from Instructions.Load_Store_Operations import LDA
from Instructions.Load_Store_Operations import LDX
from Instructions.Load_Store_Operations import LDY
from Instructions.Load_Store_Operations import STA
from Instructions.Load_Store_Operations import STX
from Instructions.Load_Store_Operations import STY

Load_Store_Operations_Dictionary = {
        LDA.INDIRECT_X.OPCODE.get_hex_value(): LDA.INDIRECT_X.INDIRECT_X,
        LDA.ZERO_PAGE.OPCODE.get_hex_value(): LDA.ZERO_PAGE.ZERO_PAGE,
        LDA.IMMEDIATE.OPCODE.get_hex_value(): LDA.IMMEDIATE.IMMEDIATE,
        LDA.ABSOLUTE.OPCODE.get_hex_value(): LDA.ABSOLUTE.ABSOLUTE,
        LDA.INDIRECT_Y.OPCODE.get_hex_value(): LDA.INDIRECT_Y.INDIRECT_Y,
        LDA.ZERO_PAGE_X.OPCODE.get_hex_value(): LDA.ZERO_PAGE_X.ZERO_PAGE_X,
        LDA.ABSOLUTE_Y.OPCODE.get_hex_value(): LDA.ABSOLUTE_Y.ABSOLUTE_Y,
        LDA.ABSOLUTE_X.OPCODE.get_hex_value(): LDA.ABSOLUTE_X.ABSOLUTE_X,

        LDX.IMMEDIATE.OPCODE.get_hex_value(): LDX.IMMEDIATE.IMMEDIATE,
        LDX.ZERO_PAGE.OPCODE.get_hex_value(): LDX.ZERO_PAGE.ZERO_PAGE,
        LDX.ABSOLUTE.OPCODE.get_hex_value(): LDX.ABSOLUTE.ABSOLUTE,
        LDX.ZERO_PAGE_Y.OPCODE.get_hex_value(): LDX.ZERO_PAGE_Y.ZERO_PAGE_Y,
        LDX.ABSOLUTE_Y.OPCODE.get_hex_value(): LDX.ABSOLUTE_Y.ABSOLUTE_Y,

        LDY.IMMEDIATE.OPCODE.get_hex_value(): LDY.IMMEDIATE.IMMEDIATE,
        LDY.ZERO_PAGE.OPCODE.get_hex_value(): LDY.ZERO_PAGE.ZERO_PAGE,
        LDY.ABSOLUTE.OPCODE.get_hex_value(): LDY.ABSOLUTE.ABSOLUTE,
        LDY.ZERO_PAGE_X.OPCODE.get_hex_value(): LDY.ZERO_PAGE_X.ZERO_PAGE_X,
        LDY.ABSOLUTE_X.OPCODE.get_hex_value(): LDY.ABSOLUTE_X.ABSOLUTE_X,

        STA.INDIRECT_X.OPCODE.get_hex_value(): STA.INDIRECT_X.INDIRECT_X,
        STA.ZERO_PAGE.OPCODE.get_hex_value(): STA.ZERO_PAGE.ZERO_PAGE,
        STA.ABSOLUTE.OPCODE.get_hex_value(): STA.ABSOLUTE.ABSOLUTE,
        STA.INDIRECT_Y.OPCODE.get_hex_value(): STA.INDIRECT_Y.INDIRECT_Y,
        STA.ZERO_PAGE_X.OPCODE.get_hex_value(): STA.ZERO_PAGE_X.ZERO_PAGE_X,
        STA.ABSOLUTE_Y.OPCODE.get_hex_value(): STA.ABSOLUTE_Y.ABSOLUTE_Y,
        STA.ABSOLUTE_X.OPCODE.get_hex_value(): STA.ABSOLUTE_X.ABSOLUTE_X,

        STX.ZERO_PAGE.OPCODE.get_hex_value(): STX.ZERO_PAGE.ZERO_PAGE,
        STX.ABSOLUTE.OPCODE.get_hex_value(): STX.ABSOLUTE.ABSOLUTE,
        STX.ZERO_PAGE_Y.OPCODE.get_hex_value(): STX.ZERO_PAGE_Y.ZERO_PAGE_Y,

        STY.ZERO_PAGE.OPCODE.get_hex_value(): STY.ZERO_PAGE.ZERO_PAGE,
        STY.ABSOLUTE.OPCODE.get_hex_value(): STY.ABSOLUTE.ABSOLUTE,
        STY.ZERO_PAGE_X.OPCODE.get_hex_value(): STY.ZERO_PAGE_X.ZERO_PAGE_X
}
