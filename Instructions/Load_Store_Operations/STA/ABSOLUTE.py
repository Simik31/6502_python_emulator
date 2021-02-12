# ######################################
#  Copyright (c) 2021                  #
#                                      #
#  Author: Martin Šimara               #
#  Last modified on 12.2.2021          #
# ######################################

from Memory import Byte

OPCODE = Byte(0x8D)
CYCLES = 4


def ABSOLUTE(cpu):
    cpu.write_byte(cpu.fetch_word(), cpu.get_register_A())
