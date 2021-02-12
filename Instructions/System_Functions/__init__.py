# ##############################
#  Copyright (c) 2021          #
#                              #
#  Author: Martin Šimara       #
#  Last modified on 12.2.2021  #
# ##############################

"""
The remaining instructions perform useful but rarely used functions.
"""

from Instructions.System_Functions import NOP

System_Functions_Dictionary = {
    NOP.IMPLIED.OPCODE.get_hex_value(): NOP.IMPLIED.IMPLIED
}
