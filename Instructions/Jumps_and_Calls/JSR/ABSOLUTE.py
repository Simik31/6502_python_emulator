# ##############################
#  Copyright (c) 2021          #
#                              #
#  Author: Martin Šimara       #
#  Last modified on 12.2.2021  #
# ##############################

from Memory import Byte


OPCODE = Byte(0x20)
CYCLES = 6


def ABSOLUTE(cpu):
    program_counter = cpu.get_PC() - 1
    cpu.write_to_stack(program_counter.get_least_significant_byte())
    cpu.write_to_stack(program_counter.get_most_significant_byte())
    cpu.set_PC(cpu.fetch_word())
    cpu.cycles -= 3
