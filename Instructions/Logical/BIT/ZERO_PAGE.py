# ######################################
#  Copyright (c) 2021                  #
#                                      #
#  Author: Martin Šimara               #
#  Last modified on 12.2.2021          #
# ######################################

from Memory import Byte


OPCODE = Byte(0x24)
CYCLES = 3


def ZERO_PAGE(cpu):
    value = cpu.read_byte(cpu.fetch_byte())
    cpu.set_mask_register_F(int((cpu.get_register_A() & value).get_value() == 0), cpu.ZERO_FLAG)
    cpu.set_mask_register_F(value.get_bit(0), cpu.NEGATIVE_FLAG)
    cpu.set_mask_register_F(value.get_bit(1), cpu.OVERFLOW_FLAG)
