# ######################################
#  Copyright (c) 2021                  #
#                                      #
#  Author: Martin Šimara               #
#  Last modified on 12.2.2021          #
# ######################################

"""
JSR - Jump to Subroutine
The JSR instruction pushes the address (minus one) of the return point on to the stack and then sets the program
counter to the target memory address.
"""

from Instructions.Jumps_and_Calls.JSR import ABSOLUTE