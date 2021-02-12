# ######################################
#  Copyright (c) 2021                  #
#                                      #
#  Author: Martin Šimara               #
#  Last modified on 12.2.2021          #
# ######################################

from Memory import Byte

OPCODE = Byte(0x39)
CYCLES = 4
CYCLES_CROSSED_PAGE = 5


def ABSOLUTE_Y(cpu):
    old_address = cpu.fetch_word()
    new_address = old_address + cpu.get_register_Y()
    if new_address.get_most_significant_byte_value() > old_address.get_most_significant_byte_value():
        cpu.cycles -= 1
    value = cpu.get_register_A() & cpu.read_byte(new_address)
    cpu.set_register_A(value)
    cpu.set_mask_register_F((1 if value.get_value() == 0 else 0), cpu.ZERO_FLAG)
    cpu.set_mask_register_F((1 if value.get_bit(0) == 1 else 0), cpu.NEGATIVE_FLAG)
