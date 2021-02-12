# ######################################
#  Copyright (c) 2021                  #
#                                      #
#  Author: Martin Šimara               #
#  Last modified on 12.2.2021          #
# ######################################

from Memory import Byte

OPCODE = Byte(0x99)
CYCLES = 5


def ABSOLUTE_Y(cpu):
    cpu.write_byte(cpu.fetch_word() + cpu.get_register_Y(), cpu.get_register_A())
