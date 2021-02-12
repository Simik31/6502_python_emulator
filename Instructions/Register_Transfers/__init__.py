# ##############################
#  Copyright (c) 2021          #
#                              #
#  Author: Martin Šimara       #
#  Last modified on 12.2.2021  #
# ##############################

"""
The contents of the X and Y registers can be moved to or from the accumulator,
setting the negative (N) and zero (Z) flags as appropriate.
"""

from Instructions.Register_Transfers import TAX
from Instructions.Register_Transfers import TAY
from Instructions.Register_Transfers import TXA
from Instructions.Register_Transfers import TYA

Register_Transfers_Dictionary = {
    TAX.IMPLIED.OPCODE.get_hex_value(): TAX.IMPLIED.IMPLIED,

    TAY.IMPLIED.OPCODE.get_hex_value(): TAY.IMPLIED.IMPLIED,

    TXA.IMPLIED.OPCODE.get_hex_value(): TXA.IMPLIED.IMPLIED,

    TYA.IMPLIED.OPCODE.get_hex_value(): TYA.IMPLIED.IMPLIED
}
