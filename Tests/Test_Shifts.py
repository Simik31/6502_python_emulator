# ##############################
#  Copyright (c) 2021          #
#                              #
#  Author: Martin Šimara       #
#  Last modified on 12.2.2021  #
# ##############################

import unittest

from Instructions.Shifts import ASL, LSR
from Memory import Byte
from Tests.Testing_constants import T_Reset_cpu, Expected_no_flag_byte, execute_and_assert


class Test_ASL(unittest.TestCase):
    Expected_zero_flag_byte = Byte(0x00)
    Expected_negative_flag_byte = Byte(0x41)
    Expected_cary_flag_byte = Byte(0x81)
    Expected_cary_and_zero_flag_byte = Byte(0x80)
    Expected_cary_and_negative_flag_byte = Byte(0xc1)

    def setUp(self) -> None:
        self.cpu = T_Reset_cpu()

    def test_ZERO_PAGE_no_flag(self):
        self.cpu.write_byte(0x0010, Expected_no_flag_byte)
        self.cpu.write_byte(0x0200, ASL.ZERO_PAGE.OPCODE)
        self.cpu.write_byte(0x0201, 0x10)

        self.cycles = ASL.ZERO_PAGE.CYCLES
        self.e_reg = '0x0010'
        self.e_val = (Expected_no_flag_byte << 1).get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ASL Zero Page"

    def test_ZERO_PAGE_zero_flag(self):
        self.cpu.write_byte(0x0010, self.Expected_zero_flag_byte)
        self.cpu.write_byte(0x0200, ASL.ZERO_PAGE.OPCODE)
        self.cpu.write_byte(0x0201, 0x10)

        self.cycles = ASL.ZERO_PAGE.CYCLES
        self.e_reg = '0x0010'
        self.e_val = (self.Expected_zero_flag_byte << 1).get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ASL Zero Page"

    def test_ZERO_PAGE_negative_flag(self):
        self.cpu.write_byte(0x0010, self.Expected_negative_flag_byte)
        self.cpu.write_byte(0x0200, ASL.ZERO_PAGE.OPCODE)
        self.cpu.write_byte(0x0201, 0x10)

        self.cycles = ASL.ZERO_PAGE.CYCLES
        self.e_reg = '0x0010'
        self.e_val = (self.Expected_negative_flag_byte << 1).get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ASL Zero Page"

    def test_ZERO_PAGE_cary_flag(self):
        self.cpu.write_byte(0x0010, self.Expected_cary_flag_byte)
        self.cpu.write_byte(0x0200, ASL.ZERO_PAGE.OPCODE)
        self.cpu.write_byte(0x0201, 0x10)

        self.cycles = ASL.ZERO_PAGE.CYCLES
        self.e_reg = '0x0010'
        self.e_val = (self.Expected_cary_flag_byte << 1).get_hex_value()
        self.mode = 'c'
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ASL Zero Page"

    def test_ZERO_PAGE_cary_and_zero_flag(self):
        self.cpu.write_byte(0x0010, self.Expected_cary_and_zero_flag_byte)
        self.cpu.write_byte(0x0200, ASL.ZERO_PAGE.OPCODE)
        self.cpu.write_byte(0x0201, 0x10)

        self.cycles = ASL.ZERO_PAGE.CYCLES
        self.e_reg = '0x0010'
        self.e_val = (self.Expected_cary_and_zero_flag_byte << 1).get_hex_value()
        self.mode = 'c+0'
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ASL Zero Page"

    def test_ZERO_PAGE_cary_and_negative_flag(self):
        self.cpu.write_byte(0x0010, self.Expected_cary_and_negative_flag_byte)
        self.cpu.write_byte(0x0200, ASL.ZERO_PAGE.OPCODE)
        self.cpu.write_byte(0x0201, 0x10)

        self.cycles = ASL.ZERO_PAGE.CYCLES
        self.e_reg = '0x0010'
        self.e_val = (self.Expected_cary_and_negative_flag_byte << 1).get_hex_value()
        self.mode = 'c-1'
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ASL Zero Page"

    def test_ACCUMULATOR_no_flag(self):
        self.cpu.set_register_A(Expected_no_flag_byte)
        self.cpu.write_byte(0x0200, ASL.ACCUMULATOR.OPCODE)

        self.cycles = ASL.ACCUMULATOR.CYCLES
        self.e_reg = 'A'
        self.e_val = (Expected_no_flag_byte << 1).get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ASL Accumulator"

    def test_ACCUMULATOR_zero_flag(self):
        self.cpu.set_register_A(self.Expected_zero_flag_byte)
        self.cpu.write_byte(0x0200, ASL.ACCUMULATOR.OPCODE)

        self.cycles = ASL.ACCUMULATOR.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(self.Expected_zero_flag_byte).get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ASL Accumulator"

    def test_ACCUMULATOR_negative_flag(self):
        self.cpu.set_register_A(self.Expected_negative_flag_byte)
        self.cpu.write_byte(0x0200, ASL.ACCUMULATOR.OPCODE)

        self.cycles = ASL.ACCUMULATOR.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(self.Expected_negative_flag_byte << 1).get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ASL Accumulator"

    def test_ACCUMULATOR_cary_flag(self):
        self.cpu.set_register_A(self.Expected_cary_flag_byte)
        self.cpu.write_byte(0x0200, ASL.ACCUMULATOR.OPCODE)

        self.cycles = ASL.ACCUMULATOR.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(self.Expected_cary_flag_byte << 1).get_hex_value()
        self.mode = 'c'
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ASL Accumulator"

    def test_ACCUMULATOR_cary_and_zero_flag(self):
        self.cpu.set_register_A(self.Expected_cary_and_zero_flag_byte)
        self.cpu.write_byte(0x0200, ASL.ACCUMULATOR.OPCODE)

        self.cycles = ASL.ACCUMULATOR.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(self.Expected_cary_and_zero_flag_byte << 1).get_hex_value()
        self.mode = 'c+0'
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ASL Accumulator"

    def test_ACCUMULATOR_cary_and_negative_flag(self):
        self.cpu.set_register_A(self.Expected_cary_and_negative_flag_byte)
        self.cpu.write_byte(0x0200, ASL.ACCUMULATOR.OPCODE)

        self.cycles = ASL.ACCUMULATOR.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(self.Expected_cary_and_negative_flag_byte << 1).get_hex_value()
        self.mode = 'c-1'
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ASL Accumulator"

    def test_ABSOLUTE_no_flag(self):
        self.cpu.write_byte(0x02f0, Expected_no_flag_byte)
        self.cpu.write_byte(0x0200, ASL.ABSOLUTE.OPCODE)
        self.cpu.write_word(0x0201, 0x02f0)

        self.cycles = ASL.ABSOLUTE.CYCLES
        self.e_reg = '0x02f0'
        self.e_val = (Expected_no_flag_byte << 1).get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ASL Absolute"

    def test_ABSOLUTE_zero_flag(self):
        self.cpu.write_byte(0x02f0, self.Expected_zero_flag_byte)
        self.cpu.write_byte(0x0200, ASL.ABSOLUTE.OPCODE)
        self.cpu.write_word(0x0201, 0x02f0)

        self.cycles = ASL.ABSOLUTE.CYCLES
        self.e_reg = '0x02f0'
        self.e_val = (self.Expected_zero_flag_byte << 1).get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ASL Absolute"

    def test_ABSOLUTE_negative_flag(self):
        self.cpu.write_byte(0x02f0, self.Expected_negative_flag_byte)
        self.cpu.write_byte(0x0200, ASL.ABSOLUTE.OPCODE)
        self.cpu.write_word(0x0201, 0x02f0)

        self.cycles = ASL.ABSOLUTE.CYCLES
        self.e_reg = '0x02f0'
        self.e_val = (self.Expected_negative_flag_byte << 1).get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ASL Absolute"

    def test_ABSOLUTE_cary_flag(self):
        self.cpu.write_byte(0x02f0, self.Expected_cary_flag_byte)
        self.cpu.write_byte(0x0200, ASL.ABSOLUTE.OPCODE)
        self.cpu.write_word(0x0201, 0x02f0)

        self.cycles = ASL.ABSOLUTE.CYCLES
        self.e_reg = '0x02f0'
        self.e_val = (self.Expected_cary_flag_byte << 1).get_hex_value()
        self.mode = 'c'
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ASL Absolute"

    def test_ABSOLUTE_cary_and_zero_flag(self):
        self.cpu.write_byte(0x02f0, self.Expected_cary_and_zero_flag_byte)
        self.cpu.write_byte(0x0200, ASL.ABSOLUTE.OPCODE)
        self.cpu.write_word(0x0201, 0x02f0)

        self.cycles = ASL.ABSOLUTE.CYCLES
        self.e_reg = '0x02f0'
        self.e_val = (self.Expected_cary_and_zero_flag_byte << 1).get_hex_value()
        self.mode = 'c+0'
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ASL Absolute"

    def test_ABSOLUTE_cary_and_negative_flag(self):
        self.cpu.write_byte(0x02f0, self.Expected_cary_and_negative_flag_byte)
        self.cpu.write_byte(0x0200, ASL.ABSOLUTE.OPCODE)
        self.cpu.write_word(0x0201, 0x02f0)

        self.cycles = ASL.ABSOLUTE.CYCLES
        self.e_reg = '0x02f0'
        self.e_val = (self.Expected_cary_and_negative_flag_byte << 1).get_hex_value()
        self.mode = 'c-1'
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ASL Absolute"

    def test_ZERO_PAGE_X_no_flag(self):
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x0015, Expected_no_flag_byte)
        self.cpu.write_byte(0x0200, ASL.ZERO_PAGE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0x10)

        self.cycles = ASL.ZERO_PAGE_X.CYCLES
        self.e_reg = '0x0015'
        self.e_val = (Expected_no_flag_byte << 1).get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ASL Zero Page X"

    def test_ZERO_PAGE_X_zero_flag(self):
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x0015, self.Expected_zero_flag_byte)
        self.cpu.write_byte(0x0200, ASL.ZERO_PAGE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0x10)

        self.cycles = ASL.ZERO_PAGE_X.CYCLES
        self.e_reg = '0x0015'
        self.e_val = (self.Expected_zero_flag_byte << 1).get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ASL Zero Page X"

    def test_ZERO_PAGE_X_negative_flag(self):
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x0015, self.Expected_negative_flag_byte)
        self.cpu.write_byte(0x0200, ASL.ZERO_PAGE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0x10)

        self.cycles = ASL.ZERO_PAGE_X.CYCLES
        self.e_reg = '0x0015'
        self.e_val = (self.Expected_negative_flag_byte << 1).get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ASL Zero Page X"

    def test_ZERO_PAGE_X_cary_flag(self):
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x0015, self.Expected_cary_flag_byte)
        self.cpu.write_byte(0x0200, ASL.ZERO_PAGE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0x10)

        self.cycles = ASL.ZERO_PAGE_X.CYCLES
        self.e_reg = '0x0015'
        self.e_val = (self.Expected_cary_flag_byte << 1).get_hex_value()
        self.mode = 'c'
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ASL Zero Page X"

    def test_ZERO_PAGE_X_cary_and_zero_flag(self):
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x0015, self.Expected_cary_and_zero_flag_byte)
        self.cpu.write_byte(0x0200, ASL.ZERO_PAGE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0x10)

        self.cycles = ASL.ZERO_PAGE_X.CYCLES
        self.e_reg = '0x0015'
        self.e_val = (self.Expected_cary_and_zero_flag_byte << 1).get_hex_value()
        self.mode = 'c+0'
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ASL Zero Page X"

    def test_ZERO_PAGE_X_cary_and_negative_flag(self):
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x0015, self.Expected_cary_and_negative_flag_byte)
        self.cpu.write_byte(0x0200, ASL.ZERO_PAGE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0x10)

        self.cycles = ASL.ZERO_PAGE_X.CYCLES
        self.e_reg = '0x0015'
        self.e_val = (self.Expected_cary_and_negative_flag_byte << 1).get_hex_value()
        self.mode = 'c-1'
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ASL Zero Page X"

    def test_ABSOLUTE_X_no_flag(self):
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x02f5, Expected_no_flag_byte)
        self.cpu.write_byte(0x0200, ASL.ABSOLUTE_X.OPCODE)
        self.cpu.write_word(0x0201, 0x02f0)

        self.cycles = ASL.ABSOLUTE_X.CYCLES
        self.e_reg = '0x02f5'
        self.e_val = (Expected_no_flag_byte << 1).get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ASL Absolute X"

    def test_ABSOLUTE_X_zero_flag(self):
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x02f5, self.Expected_zero_flag_byte)
        self.cpu.write_byte(0x0200, ASL.ABSOLUTE_X.OPCODE)
        self.cpu.write_word(0x0201, 0x02f0)

        self.cycles = ASL.ABSOLUTE_X.CYCLES
        self.e_reg = '0x02f5'
        self.e_val = (self.Expected_zero_flag_byte << 1).get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ASL Absolute X"

    def test_ABSOLUTE_X_negative_flag(self):
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x02f5, self.Expected_negative_flag_byte)
        self.cpu.write_byte(0x0200, ASL.ABSOLUTE_X.OPCODE)
        self.cpu.write_word(0x0201, 0x02f0)

        self.cycles = ASL.ABSOLUTE_X.CYCLES
        self.e_reg = '0x02f5'
        self.e_val = (self.Expected_negative_flag_byte << 1).get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ASL Absolute X"

    def test_ABSOLUTE_X_cary_flag(self):
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x02f5, self.Expected_cary_flag_byte)
        self.cpu.write_byte(0x0200, ASL.ABSOLUTE_X.OPCODE)
        self.cpu.write_word(0x0201, 0x02f0)

        self.cycles = ASL.ABSOLUTE_X.CYCLES
        self.e_reg = '0x02f5'
        self.e_val = (self.Expected_cary_flag_byte << 1).get_hex_value()
        self.mode = 'c'
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ASL Absolute"

    def test_ABSOLUTE_X_cary_and_zero_flag(self):
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x02f5, self.Expected_cary_and_zero_flag_byte)
        self.cpu.write_byte(0x0200, ASL.ABSOLUTE_X.OPCODE)
        self.cpu.write_word(0x0201, 0x02f0)

        self.cycles = ASL.ABSOLUTE_X.CYCLES
        self.e_reg = '0x02f5'
        self.e_val = (self.Expected_cary_and_zero_flag_byte << 1).get_hex_value()
        self.mode = 'c+0'
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ASL Absolute X"

    def test_ABSOLUTE_X_cary_and_negative_flag(self):
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x02f5, self.Expected_cary_and_negative_flag_byte)
        self.cpu.write_byte(0x0200, ASL.ABSOLUTE_X.OPCODE)
        self.cpu.write_word(0x0201, 0x02f0)

        self.cycles = ASL.ABSOLUTE_X.CYCLES
        self.e_reg = '0x02f5'
        self.e_val = (self.Expected_cary_and_negative_flag_byte << 1).get_hex_value()
        self.mode = 'c-1'
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ASL Absolute X"

    def tearDown(self) -> None:
        e, a, m = execute_and_assert(self.cpu, self.cycles, self.e_reg, self.e_val,
                                     self.flags, self.test_name, self.mode)
        self.assertEqual(e, a, m)


class Test_LSR(unittest.TestCase):
    Expected_no_flag_byte = Byte(0x30)
    Expected_zero_flag_byte = Byte(0x00)
    Expected_cary_flag_byte = Byte(0x81)
    Expected_cary_and_zero_flag_byte = Byte(0x01)

    def setUp(self) -> None:
        self.cpu = T_Reset_cpu()

    def test_ZERO_PAGE_no_flag(self):
        self.cpu.write_byte(0x0010, self.Expected_no_flag_byte)
        self.cpu.write_byte(0x0200, LSR.ZERO_PAGE.OPCODE)
        self.cpu.write_byte(0x0201, 0x10)

        self.cycles = LSR.ZERO_PAGE.CYCLES
        self.e_reg = '0x0010'
        self.e_val = (self.Expected_no_flag_byte >> 1).get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test LSR Zero Page"

    def test_ZERO_PAGE_zero_flag(self):
        self.cpu.write_byte(0x0010, self.Expected_zero_flag_byte)
        self.cpu.write_byte(0x0200, LSR.ZERO_PAGE.OPCODE)
        self.cpu.write_byte(0x0201, 0x10)

        self.cycles = LSR.ZERO_PAGE.CYCLES
        self.e_reg = '0x0010'
        self.e_val = (self.Expected_zero_flag_byte >> 1).get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test LSR Zero Page"

    def test_ZERO_PAGE_cary_flag(self):
        self.cpu.write_byte(0x0010, self.Expected_cary_flag_byte)
        self.cpu.write_byte(0x0200, LSR.ZERO_PAGE.OPCODE)
        self.cpu.write_byte(0x0201, 0x10)

        self.cycles = LSR.ZERO_PAGE.CYCLES
        self.e_reg = '0x0010'
        self.e_val = (self.Expected_cary_flag_byte >> 1).get_hex_value()
        self.mode = 'c'
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test LSR Zero Page"

    def test_ZERO_PAGE_cary_and_zero_flag(self):
        self.cpu.write_byte(0x0010, self.Expected_cary_and_zero_flag_byte)
        self.cpu.write_byte(0x0200, LSR.ZERO_PAGE.OPCODE)
        self.cpu.write_byte(0x0201, 0x10)

        self.cycles = LSR.ZERO_PAGE.CYCLES
        self.e_reg = '0x0010'
        self.e_val = (self.Expected_cary_and_zero_flag_byte >> 1).get_hex_value()
        self.mode = 'c+0'
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test LSR Zero Page"

    def test_ACCUMULATOR_no_flag(self):
        self.cpu.set_register_A(self.Expected_no_flag_byte)
        self.cpu.write_byte(0x0200, LSR.ACCUMULATOR.OPCODE)

        self.cycles = LSR.ACCUMULATOR.CYCLES
        self.e_reg = 'A'
        self.e_val = (self.Expected_no_flag_byte >> 1).get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test LSR Accumulator"

    def test_ACCUMULATOR_zero_flag(self):
        self.cpu.set_register_A(self.Expected_zero_flag_byte)
        self.cpu.write_byte(0x0200, LSR.ACCUMULATOR.OPCODE)

        self.cycles = LSR.ACCUMULATOR.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(self.Expected_zero_flag_byte).get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test LSR Accumulator"

    def test_ACCUMULATOR_cary_flag(self):
        self.cpu.set_register_A(self.Expected_cary_flag_byte)
        self.cpu.write_byte(0x0200, LSR.ACCUMULATOR.OPCODE)

        self.cycles = LSR.ACCUMULATOR.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(self.Expected_cary_flag_byte >> 1).get_hex_value()
        self.mode = 'c'
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test LSR Accumulator"

    def test_ACCUMULATOR_cary_and_zero_flag(self):
        self.cpu.set_register_A(self.Expected_cary_and_zero_flag_byte)
        self.cpu.write_byte(0x0200, LSR.ACCUMULATOR.OPCODE)

        self.cycles = LSR.ACCUMULATOR.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(self.Expected_cary_and_zero_flag_byte >> 1).get_hex_value()
        self.mode = 'c+0'
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test LSR Accumulator"

    def test_ABSOLUTE_no_flag(self):
        self.cpu.write_byte(0x02f0, self.Expected_no_flag_byte)
        self.cpu.write_byte(0x0200, LSR.ABSOLUTE.OPCODE)
        self.cpu.write_word(0x0201, 0x02f0)

        self.cycles = LSR.ABSOLUTE.CYCLES
        self.e_reg = '0x02f0'
        self.e_val = (self.Expected_no_flag_byte >> 1).get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test LSR Absolute"

    def test_ABSOLUTE_zero_flag(self):
        self.cpu.write_byte(0x02f0, self.Expected_zero_flag_byte)
        self.cpu.write_byte(0x0200, LSR.ABSOLUTE.OPCODE)
        self.cpu.write_word(0x0201, 0x02f0)

        self.cycles = LSR.ABSOLUTE.CYCLES
        self.e_reg = '0x02f0'
        self.e_val = (self.Expected_zero_flag_byte >> 1).get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test LSR Absolute"

    def test_ABSOLUTE_cary_flag(self):
        self.cpu.write_byte(0x02f0, self.Expected_cary_flag_byte)
        self.cpu.write_byte(0x0200, LSR.ABSOLUTE.OPCODE)
        self.cpu.write_word(0x0201, 0x02f0)

        self.cycles = LSR.ABSOLUTE.CYCLES
        self.e_reg = '0x02f0'
        self.e_val = (self.Expected_cary_flag_byte >> 1).get_hex_value()
        self.mode = 'c'
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test LSR Absolute"

    def test_ABSOLUTE_cary_and_zero_flag(self):
        self.cpu.write_byte(0x02f0, self.Expected_cary_and_zero_flag_byte)
        self.cpu.write_byte(0x0200, LSR.ABSOLUTE.OPCODE)
        self.cpu.write_word(0x0201, 0x02f0)

        self.cycles = LSR.ABSOLUTE.CYCLES
        self.e_reg = '0x02f0'
        self.e_val = (self.Expected_cary_and_zero_flag_byte >> 1).get_hex_value()
        self.mode = 'c+0'
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test LSR Absolute"

    def test_ZERO_PAGE_X_no_flag(self):
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x0015, self.Expected_no_flag_byte)
        self.cpu.write_byte(0x0200, LSR.ZERO_PAGE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0x10)

        self.cycles = LSR.ZERO_PAGE_X.CYCLES
        self.e_reg = '0x0015'
        self.e_val = (self.Expected_no_flag_byte >> 1).get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test LSR Zero Page X"

    def test_ZERO_PAGE_X_zero_flag(self):
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x0015, self.Expected_zero_flag_byte)
        self.cpu.write_byte(0x0200, LSR.ZERO_PAGE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0x10)

        self.cycles = LSR.ZERO_PAGE_X.CYCLES
        self.e_reg = '0x0015'
        self.e_val = (self.Expected_zero_flag_byte >> 1).get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test LSR Zero Page X"

    def test_ZERO_PAGE_X_cary_flag(self):
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x0015, self.Expected_cary_flag_byte)
        self.cpu.write_byte(0x0200, LSR.ZERO_PAGE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0x10)

        self.cycles = LSR.ZERO_PAGE_X.CYCLES
        self.e_reg = '0x0015'
        self.e_val = (self.Expected_cary_flag_byte >> 1).get_hex_value()
        self.mode = 'c'
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test LSR Zero Page X"

    def test_ZERO_PAGE_X_cary_and_zero_flag(self):
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x0015, self.Expected_cary_and_zero_flag_byte)
        self.cpu.write_byte(0x0200, LSR.ZERO_PAGE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0x10)

        self.cycles = LSR.ZERO_PAGE_X.CYCLES
        self.e_reg = '0x0015'
        self.e_val = (self.Expected_cary_and_zero_flag_byte >> 1).get_hex_value()
        self.mode = 'c+0'
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test LSR Zero Page X"

    def test_ABSOLUTE_X_no_flag(self):
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x02f5, self.Expected_no_flag_byte)
        self.cpu.write_byte(0x0200, LSR.ABSOLUTE_X.OPCODE)
        self.cpu.write_word(0x0201, 0x02f0)

        self.cycles = LSR.ABSOLUTE_X.CYCLES
        self.e_reg = '0x02f5'
        self.e_val = (self.Expected_no_flag_byte >> 1).get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test LSR Absolute X"

    def test_ABSOLUTE_X_zero_flag(self):
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x02f5, self.Expected_zero_flag_byte)
        self.cpu.write_byte(0x0200, LSR.ABSOLUTE_X.OPCODE)
        self.cpu.write_word(0x0201, 0x02f0)

        self.cycles = LSR.ABSOLUTE_X.CYCLES
        self.e_reg = '0x02f5'
        self.e_val = (self.Expected_zero_flag_byte >> 1).get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test LSR Absolute X"

    def test_ABSOLUTE_X_cary_flag(self):
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x02f5, self.Expected_cary_flag_byte)
        self.cpu.write_byte(0x0200, LSR.ABSOLUTE_X.OPCODE)
        self.cpu.write_word(0x0201, 0x02f0)

        self.cycles = LSR.ABSOLUTE_X.CYCLES
        self.e_reg = '0x02f5'
        self.e_val = (self.Expected_cary_flag_byte >> 1).get_hex_value()
        self.mode = 'c'
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test LSR Absolute"

    def test_ABSOLUTE_X_cary_and_zero_flag(self):
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x02f5, self.Expected_cary_and_zero_flag_byte)
        self.cpu.write_byte(0x0200, LSR.ABSOLUTE_X.OPCODE)
        self.cpu.write_word(0x0201, 0x02f0)

        self.cycles = LSR.ABSOLUTE_X.CYCLES
        self.e_reg = '0x02f5'
        self.e_val = (self.Expected_cary_and_zero_flag_byte >> 1).get_hex_value()
        self.mode = 'c+0'
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test LSR Absolute X"

    def tearDown(self) -> None:
        e, a, m = execute_and_assert(self.cpu, self.cycles, self.e_reg, self.e_val,
                                     self.flags, self.test_name, self.mode)
        self.assertEqual(e, a, m)


if __name__ == '__main__':
    unittest.main()
