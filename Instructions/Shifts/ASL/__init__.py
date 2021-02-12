# ##############################
#  Copyright (c) 2021          #
#                              #
#  Author: Martin Šimara       #
#  Last modified on 12.2.2021  #
# ##############################

"""
This operation shifts all the bits of the accumulator or memory contents one bit left.
Bit 0 is set to 0 and bit 7 is placed in the carry flag.
The effect of this operation is to multiply the memory contents by 2 (ignoring 2's complement considerations),
setting the carry if the result will not fit in 8 bits.
"""

from Instructions.Shifts.ASL import ABSOLUTE
from Instructions.Shifts.ASL import ABSOLUTE_X
from Instructions.Shifts.ASL import ACCUMULATOR
from Instructions.Shifts.ASL import ZERO_PAGE
from Instructions.Shifts.ASL import ZERO_PAGE_X
