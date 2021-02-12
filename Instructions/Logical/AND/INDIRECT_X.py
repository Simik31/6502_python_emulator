# ##############################
#  Copyright (c) 2021          #
#                              #
#  Author: Martin Šimara       #
#  Last modified on 12.2.2021  #
# ##############################

from Memory import Byte


OPCODE = Byte(0x21)
CYCLES = 6


def INDIRECT_X(cpu):
    value = cpu.read_byte(cpu.read_word(cpu.fetch_byte() + cpu.get_register_X())) & cpu.get_register_A()
    cpu.set_register_A(value)
    cpu.cycles -= 1
    cpu.set_mask_register_F((1 if value.get_value() == 0 else 0), cpu.ZERO_FLAG)
    cpu.set_mask_register_F((1 if value.get_bit(0) == 1 else 0), cpu.NEGATIVE_FLAG)
