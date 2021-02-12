# ######################################
#  Copyright (c) 2021                  #
#                                      #
#  Author: Martin Šimara               #
#  Last modified on 12.2.2021          #
# ######################################

from Memory import Byte


OPCODE = Byte(0x98)
CYCLES = 2


def IMPLIED(cpu):
    value = cpu.get_register_Y()
    cpu.set_register_A(value)
    cpu.set_mask_register_F((1 if value.get_value() == 0 else 0), cpu.ZERO_FLAG)
    cpu.set_mask_register_F((1 if value.get_bit(0) == 1 else 0), cpu.NEGATIVE_FLAG)
