# ##############################
#  Copyright (c) 2021          #
#                              #
#  Author: Martin Šimara       #
#  Last modified on 12.2.2021  #
# ##############################

from Memory import Byte


OPCODE = Byte(0x28)
CYCLES = 4


def IMPLIED(cpu):
    cpu.set_register_F(cpu.read_from_stack())
