# ##############################
#  Copyright (c) 2021          #
#                              #
#  Author: Martin Šimara       #
#  Last modified on 12.2.2021  #
# ##############################

from Memory import Byte


OPCODE = Byte(0x46)
CYCLES = 5


def ZERO_PAGE(cpu):
    address = cpu.fetch_byte()
    value = cpu.read_byte(address)
    carry = value.get_bit(7)
    value = value >> 1
    cpu.write_byte(address, value)
    cpu.set_mask_register_F((1 if value.get_value() == 0 else 0), cpu.ZERO_FLAG)
    cpu.set_mask_register_F((1 if value.get_bit(0) == 1 else 0), cpu.NEGATIVE_FLAG)
    cpu.set_mask_register_F(carry, cpu.CARRY_FLAG)
