# ##############################
#  Copyright (c) 2021          #
#                              #
#  Author: Martin Šimara       #
#  Last modified on 12.2.2021  #
# ##############################

"""
Each of the bits in A or M is shift one place to the right.
The bit that was in bit 0 is shifted into the carry flag.
Bit 7 is set to zero.
"""

from Instructions.Shifts.LSR import ABSOLUTE
from Instructions.Shifts.LSR import ABSOLUTE_X
from Instructions.Shifts.LSR import ACCUMULATOR
from Instructions.Shifts.LSR import ZERO_PAGE
from Instructions.Shifts.LSR import ZERO_PAGE_X
