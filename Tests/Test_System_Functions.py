# ######################################
#  Copyright (c) 2021                  #
#                                      #
#  Author: Martin Šimara               #
#  Last modified on 31/01/2021, 13:39  #
# ######################################

import unittest
from CPU import CPU
from Memory import Word
from Instructions.System_Functions import NOP
from Testing_constants import T_Reset_cpu, execute_and_assert


class Test_NOP(unittest.TestCase):
    def setUp(self) -> None:
        self.cpu: CPU = T_Reset_cpu()

    def test_IMPLIED(self):
        self.cpu.write_byte(0x0200, NOP.IMPLIED.OPCODE)

        self.cycles = NOP.IMPLIED.CYCLES
        self.e_reg = 'PC'
        self.e_val = Word(0x0201).get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test NOP Implied"

    def tearDown(self) -> None:
        e, a, m = execute_and_assert(self.cpu, self.cycles, self.e_reg, self.e_val,
                                     self.flags, self.test_name, self.mode)
        self.assertEqual(e, a, m)


if __name__ == '__main__':
    unittest.main()
