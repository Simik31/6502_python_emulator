# ##############################
#  Copyright (c) 2021          #
#                              #
#  Author: Martin Šimara       #
#  Last modified on 12.2.2021  #
# ##############################

from Memory import Byte, Word

OPCODE = Byte(0x94)
CYCLES = 4


def ZERO_PAGE_X(cpu):
    old_address = Word(cpu.fetch_byte())
    new_address = old_address + cpu.get_register_X()
    if new_address.get_most_significant_byte_value() > old_address.get_most_significant_byte_value():
        cpu.cycles -= 1
    cpu.write_byte(new_address, cpu.get_register_Y())
