# ##############################
#  Copyright (c) 2021          #
#                              #
#  Author: Martin Šimara       #
#  Last modified on 12.2.2021  #
# ##############################

"""
The 6502 has a relatively basic set of instructions, many having similar functions.
The following sections list the complete set of 56 instructions in functional groups.
"""

from Instructions.Load_Store_Operations import Load_Store_Operations_Dictionary
from Instructions.Register_Transfers import Register_Transfers_Dictionary
from Instructions.Stack_Operations import Stack_Operations_Dictionary
from Instructions.Logical import Logical_Dictionary
from Instructions.Increments_and_Decrements import Increments_and_Decrements_Dictionary
from Instructions.Shifts import Shifts_Dictionary
from Instructions.Jumps_and_Calls import Jumps_and_Calls_Dictionary
from Instructions.System_Functions import System_Functions_Dictionary

from Memory import Byte


def selector(instruction: Byte):
    instruction = instruction.get_hex_value()

    if instruction in Load_Store_Operations_Dictionary:
        return Load_Store_Operations_Dictionary.get(instruction)

    if instruction in Register_Transfers_Dictionary:
        return Register_Transfers_Dictionary.get(instruction)

    if instruction in Stack_Operations_Dictionary:
        return Stack_Operations_Dictionary.get(instruction)

    if instruction in Logical_Dictionary:
        return Logical_Dictionary.get(instruction)

    if instruction in Increments_and_Decrements_Dictionary:
        return Increments_and_Decrements_Dictionary.get(instruction)

    if instruction in Shifts_Dictionary:
        return Shifts_Dictionary.get(instruction)

    if instruction in Jumps_and_Calls_Dictionary:
        return Jumps_and_Calls_Dictionary.get(instruction)

    if instruction in System_Functions_Dictionary:
        return System_Functions_Dictionary.get(instruction)

    return None
