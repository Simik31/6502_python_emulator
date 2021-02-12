# ######################################
#  Copyright (c) 2021                  #
#                                      #
#  Author: Martin Šimara               #
#  Last modified on 12.2.2021          #
# ######################################

from Memory import Byte


OPCODE = Byte(0x81)
CYCLES = 6


def INDIRECT_X(cpu):
    cpu.write_byte(cpu.read_word(cpu.fetch_byte() + cpu.get_register_X()), cpu.get_register_A())
    cpu.cycles -= 1
