# ##############################
#  Copyright (c) 2021          #
#                              #
#  Author: Martin Šimara       #
#  Last modified on 12.2.2021  #
# ##############################

from Memory import Byte

OPCODE = Byte(0x91)
CYCLES = 6


def INDIRECT_Y(cpu):
    old_address = cpu.read_word(cpu.fetch_byte())
    new_address = old_address + cpu.get_register_Y()
    if new_address.get_most_significant_byte_value() > old_address.get_most_significant_byte_value():
        cpu.cycles -= 1
    cpu.write_byte(new_address, cpu.get_register_A())
