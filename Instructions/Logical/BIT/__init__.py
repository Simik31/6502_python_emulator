# ##############################
#  Copyright (c) 2021          #
#                              #
#  Author: Martin Šimara       #
#  Last modified on 12.2.2021  #
# ##############################

"""
BIT - Bit Test
This instructions is used to test if one or more bits are set in a target memory location.
The mask pattern in A is ANDed with the value in memory to set or clear the zero flag, but the result is not kept.
Bits 7 and 6 of the value from memory are copied into the N and V flags.
"""

from Instructions.Logical.BIT import ABSOLUTE
from Instructions.Logical.BIT import ZERO_PAGE
