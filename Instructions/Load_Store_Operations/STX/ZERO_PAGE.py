# ##############################
#  Copyright (c) 2021          #
#                              #
#  Author: Martin Šimara       #
#  Last modified on 12.2.2021  #
# ##############################

from Memory import Byte


OPCODE = Byte(0x86)
CYCLES = 3


def ZERO_PAGE(cpu):
    cpu.write_byte(cpu.fetch_word(), cpu.get_register_X())
