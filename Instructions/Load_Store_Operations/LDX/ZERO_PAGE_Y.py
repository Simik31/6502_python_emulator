# ##############################
#  Copyright (c) 2021          #
#                              #
#  Author: Martin Šimara       #
#  Last modified on 12.2.2021  #
# ##############################

from Memory import Byte

OPCODE = Byte(0xb6)
CYCLES = 4


def ZERO_PAGE_Y(cpu):
    value = cpu.read_byte(cpu.fetch_byte() + cpu.get_register_Y())
    cpu.cycles -= 1
    cpu.set_register_X(value)
    cpu.set_mask_register_F((1 if value.get_value() == 0 else 0), cpu.ZERO_FLAG)
    cpu.set_mask_register_F((1 if value.get_bit(0) == 1 else 0), cpu.NEGATIVE_FLAG)
