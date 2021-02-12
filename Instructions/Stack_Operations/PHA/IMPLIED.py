# ######################################
#  Copyright (c) 2021                  #
#                                      #
#  Author: Martin Šimara               #
#  Last modified on 12.2.2021          #
# ######################################

from Memory import Byte


OPCODE = Byte(0x48)
CYCLES = 3


def IMPLIED(cpu):
    cpu.write_to_stack(cpu.get_register_A())