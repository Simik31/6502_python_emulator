# ######################################
#  Copyright (c) 2021                  #
#                                      #
#  Author: Martin Šimara               #
#  Last modified on 31/01/2021, 11:56  #
# ######################################

import unittest
from CPU import CPU
from Memory import Word
from Instructions.Load_Store_Operations import LDA
from Testing_constants import T_Reset_cpu, execute_and_assert
from Testing_constants import Expected_no_flag_byte


class Test_CPU(unittest.TestCase):
    def setUp(self) -> None:
        self.cpu: CPU = T_Reset_cpu()
        self.cpu.write_byte(0x0200, LDA.IMMEDIATE.OPCODE)
        self.flags = self.cpu.get_register_F()
        self.mode = 1

    def test_zero_cycles(self):
        self.cycles = 0
        self.e_reg = 'PC'
        self.e_val = Word(0x0200).get_hex_value()
        self.test_name = "Test zero cycles"

    def test_run_more_cycles_than_required_if_needed(self):
        self.cpu.write_byte(0x0201, Expected_no_flag_byte)

        self.cycles = 1
        self.e_reg = 'A'
        self.e_val = Expected_no_flag_byte.get_hex_value()
        self.test_name = "Test more cycles than required"

    def test_incorrect_no_instruction(self):
        self.cycles = 1
        self.e_reg = 'PC'
        self.e_val = Word(0x0202).get_hex_value()
        self.mode = 0
        self.test_name = "Test no instruction"

    def tearDown(self) -> None:
        e, a, m = execute_and_assert(self.cpu, self.cycles, self.e_reg, self.e_val,
                                     self.flags, self.test_name, self.mode)
        self.assertEqual(e, a, m)


if __name__ == '__main__':
    unittest.main()
