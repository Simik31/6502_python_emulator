# ##############################
#  Copyright (c) 2021          #
#                              #
#  Author: Martin Šimara       #
#  Last modified on 12.2.2021  #
# ##############################

import unittest
from CPU import CPU
from Instructions.Jumps_and_Calls import JSR
from Testing_constants import T_Reset_cpu, execute_and_assert
from Testing_constants import Expected_no_flag_byte


class Test_JSR(unittest.TestCase):
    def setUp(self) -> None:
        self.cpu: CPU = T_Reset_cpu()

    def test_ABSOLUTE(self):
        self.cpu.write_byte(0x0200, JSR.ABSOLUTE.OPCODE)
        self.cpu.write_byte(0x0201, Expected_no_flag_byte) # 0x0000 + Expected_no_flag_byte

        self.cycles = JSR.ABSOLUTE.CYCLES
        self.e_reg = 'PC'
        self.e_val = Expected_no_flag_byte.get_hex_value(6)
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test JSR Absolute"

    def tearDown(self) -> None:
        e, a, m = execute_and_assert(self.cpu, self.cycles, self.e_reg, self.e_val,
                                     self.flags, self.test_name, self.mode)
        self.assertEqual(e, a, m)


if __name__ == '__main__':
    unittest.main()
