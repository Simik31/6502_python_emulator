# ######################################
#  Copyright (c) 2021                  #
#                                      #
#  Author: Martin Šimara               #
#  Last modified on 12.2.2021          #
# ######################################

"""
The following instructions modify the program counter causing a break to normal sequential execution.
The JSR instruction pushes the old PC onto the stack before changing it to the new location allowing a subsequent
RTS to return execution to the instruction after the call.
"""

from Instructions.Jumps_and_Calls import JSR

Jumps_and_Calls_Dictionary = {
    JSR.ABSOLUTE.OPCODE.get_hex_value(): JSR.ABSOLUTE.ABSOLUTE
}
