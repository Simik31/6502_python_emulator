# ######################################
#  Copyright (c) 2021                  #
#                                      #
#  Author: Martin Šimara               #
#  Last modified on 12.2.2021          #
# ######################################

from Memory import Byte


OPCODE = Byte(0xea)
CYCLES = 2


def IMPLIED(cpu):
    cpu.cycles -= 1
