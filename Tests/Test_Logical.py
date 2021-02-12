# ##############################
#  Copyright (c) 2021          #
#                              #
#  Author: Martin Šimara       #
#  Last modified on 12.2.2021  #
# ##############################

import unittest

from CPU import CPU
from Memory import Byte
from Instructions.Logical import AND, EOR, ORA, BIT
from Testing_constants import T_Reset_cpu, execute_and_assert
from Testing_constants import Expected_no_flag_byte, Expected_zero_flag_byte, Expected_negative_flag_byte


class Test_AND(unittest.TestCase):
    def setUp(self) -> None:
        self.cpu: CPU = T_Reset_cpu()

    def test_INDIRECT_X_no_flag(self):
        self.cpu.set_register_A(0x81)
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x0018, 0xf0)
        self.cpu.write_byte(0x0019, 0x13)
        self.cpu.write_byte(0x0200, AND.INDIRECT_X.OPCODE)
        self.cpu.write_byte(0x0201, 0x13)
        self.cpu.write_byte(0x13f0, Expected_no_flag_byte)

        self.cycles = AND.INDIRECT_X.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_no_flag_byte & 0x81).get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test AND Zero Page"

    def test_INDIRECT_X_zero_flag(self):
        self.cpu.set_register_A(0x81)
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x0018, 0xf0)
        self.cpu.write_byte(0x0019, 0x13)
        self.cpu.write_byte(0x0200, AND.INDIRECT_X.OPCODE)
        self.cpu.write_byte(0x0201, 0x13)
        self.cpu.write_byte(0x13f0, Expected_zero_flag_byte)

        self.cycles = AND.INDIRECT_X.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_zero_flag_byte & 0x81).get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test AND Zero Page"

    def test_INDIRECT_X_negative_flag(self):
        self.cpu.set_register_A(0x81)
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x0018, 0xf0)
        self.cpu.write_byte(0x0019, 0x13)
        self.cpu.write_byte(0x0200, AND.INDIRECT_X.OPCODE)
        self.cpu.write_byte(0x0201, 0x13)
        self.cpu.write_byte(0x13f0, Expected_negative_flag_byte)

        self.cycles = AND.INDIRECT_X.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_negative_flag_byte & 0x81).get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test AND Zero Page"

    def test_ZERO_PAGE_no_flag(self):
        self.cpu.set_register_A(0x81)
        self.cpu.write_byte(0x0013, Expected_no_flag_byte)
        self.cpu.write_byte(0x0200, AND.ZERO_PAGE.OPCODE)
        self.cpu.write_byte(0x0201, 0x13)

        self.cycles = AND.ZERO_PAGE.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_no_flag_byte & 0x81).get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test AND Zero Page"

    def test_ZERO_PAGE_zero_flag(self):
        self.cpu.set_register_A(0x81)
        self.cpu.write_byte(0x0013, Expected_zero_flag_byte)
        self.cpu.write_byte(0x0200, AND.ZERO_PAGE.OPCODE)
        self.cpu.write_byte(0x0201, 0x13)

        self.cycles = AND.ZERO_PAGE.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_zero_flag_byte & 0x81).get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test AND Zero Page"

    def test_ZERO_PAGE_negative_flag(self):
        self.cpu.set_register_A(0x81)
        self.cpu.write_byte(0x0013, Expected_negative_flag_byte)
        self.cpu.write_byte(0x0200, AND.ZERO_PAGE.OPCODE)
        self.cpu.write_byte(0x0201, 0x13)

        self.cycles = AND.ZERO_PAGE.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_negative_flag_byte & 0x81).get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test AND Zero Page"

    def test_IMMEDIATE_no_flag(self):
        self.cpu.set_register_A(0x81)
        self.cpu.write_byte(0x0200, AND.IMMEDIATE.OPCODE)
        self.cpu.write_byte(0x0201, Expected_no_flag_byte)

        self.cycles = AND.IMMEDIATE.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_no_flag_byte & 0x81).get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test AND Immediate"

    def test_IMMEDIATE_zero_flag(self):
        self.cpu.set_register_A(0x81)
        self.cpu.write_byte(0x0200, AND.IMMEDIATE.OPCODE)
        self.cpu.write_byte(0x0201, Expected_zero_flag_byte)

        self.cycles = AND.IMMEDIATE.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_zero_flag_byte & 0x81).get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test AND Immediate"

    def test_IMMEDIATE_negative_flag(self):
        self.cpu.set_register_A(0x81)
        self.cpu.write_byte(0x0200, AND.IMMEDIATE.OPCODE)
        self.cpu.write_byte(0x0201, Expected_negative_flag_byte)

        self.cycles = AND.IMMEDIATE.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_negative_flag_byte & 0x81).get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test AND Immediate"

    def test_ABSOLUTE_no_flag(self):
        self.cpu.set_register_A(0x81)
        self.cpu.write_byte(0x0200, AND.ABSOLUTE.OPCODE)
        self.cpu.write_byte(0x0201, 0xff)
        self.cpu.write_byte(0x0202, 0x13)
        self.cpu.write_byte(0x13ff, Expected_no_flag_byte)

        self.cycles = AND.ABSOLUTE.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_no_flag_byte & 0x81).get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test AND Absolute"

    def test_ABSOLUTE_zero_flag(self):
        self.cpu.set_register_A(0x81)
        self.cpu.write_byte(0x0200, AND.ABSOLUTE.OPCODE)
        self.cpu.write_byte(0x0201, 0xff)
        self.cpu.write_byte(0x0202, 0x13)
        self.cpu.write_byte(0x13ff, Expected_zero_flag_byte)

        self.cycles = AND.ABSOLUTE.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_zero_flag_byte & 0x81).get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test AND Absolute"

    def test_ABSOLUTE_negative_flag(self):
        self.cpu.set_register_A(0x81)
        self.cpu.write_byte(0x0200, AND.ABSOLUTE.OPCODE)
        self.cpu.write_byte(0x0201, 0xff)
        self.cpu.write_byte(0x0202, 0x13)
        self.cpu.write_byte(0x13ff, Expected_negative_flag_byte)

        self.cycles = AND.ABSOLUTE.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_negative_flag_byte & 0x81).get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test AND Absolute"

    def test_INDIRECT_Y_no_flag(self):
        self.cpu.set_register_A(0x81)
        self.cpu.set_register_Y(0x05)
        self.cpu.write_byte(0x0013, 0xf0)
        self.cpu.write_byte(0x0014, 0x13)
        self.cpu.write_byte(0x0200, AND.INDIRECT_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0x13)
        self.cpu.write_byte(0x13f5, Expected_no_flag_byte)

        self.cycles = AND.INDIRECT_Y.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_no_flag_byte & 0x81).get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test AND Zero Page"

    def test_INDIRECT_Y_CROSSED_PAGE_no_flag(self):
        self.cpu.set_register_A(0x81)
        self.cpu.set_register_Y(0x05)
        self.cpu.write_byte(0x0013, 0xff)
        self.cpu.write_byte(0x0014, 0x13)
        self.cpu.write_byte(0x0200, AND.INDIRECT_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0x13)
        self.cpu.write_byte(0x1404, Expected_no_flag_byte)

        self.cycles = AND.INDIRECT_Y.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_no_flag_byte & 0x81).get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test AND Zero Page"

    def test_INDIRECT_Y_zero_flag(self):
        self.cpu.set_register_A(0x81)
        self.cpu.set_register_Y(0x05)
        self.cpu.write_byte(0x0013, 0xf0)
        self.cpu.write_byte(0x0014, 0x13)
        self.cpu.write_byte(0x0200, AND.INDIRECT_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0x13)
        self.cpu.write_byte(0x13f5, Expected_zero_flag_byte)

        self.cycles = AND.INDIRECT_Y.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_zero_flag_byte & 0x81).get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test AND Zero Page"

    def test_INDIRECT_Y_CROSSED_PAGE_zero_flag(self):
        self.cpu.set_register_A(0x81)
        self.cpu.set_register_Y(0x05)
        self.cpu.write_byte(0x0013, 0xff)
        self.cpu.write_byte(0x0014, 0x13)
        self.cpu.write_byte(0x0200, AND.INDIRECT_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0x13)
        self.cpu.write_byte(0x1404, Expected_zero_flag_byte)

        self.cycles = AND.INDIRECT_Y.CYCLES_CROSSED_PAGE
        self.e_reg = 'A'
        self.e_val = Byte(Expected_zero_flag_byte & 0x81).get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test AND Zero Page"

    def test_INDIRECT_Y_negative_flag(self):
        self.cpu.set_register_A(0x81)
        self.cpu.set_register_Y(0x05)
        self.cpu.write_byte(0x0013, 0xf0)
        self.cpu.write_byte(0x0014, 0x13)
        self.cpu.write_byte(0x0200, AND.INDIRECT_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0x13)
        self.cpu.write_byte(0x13f5, Expected_negative_flag_byte)

        self.cycles = AND.INDIRECT_Y.CYCLES_CROSSED_PAGE
        self.e_reg = 'A'
        self.e_val = Byte(Expected_negative_flag_byte & 0x81).get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test AND Zero Page"

    def test_INDIRECT_Y_CROSSED_PAGE_negative_flag(self):
        self.cpu.set_register_A(0x81)
        self.cpu.set_register_Y(0x05)
        self.cpu.write_byte(0x0013, 0xff)
        self.cpu.write_byte(0x0014, 0x13)
        self.cpu.write_byte(0x0200, AND.INDIRECT_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0x13)
        self.cpu.write_byte(0x1404, Expected_negative_flag_byte)

        self.cycles = AND.INDIRECT_Y.CYCLES_CROSSED_PAGE
        self.e_reg = 'A'
        self.e_val = Byte(Expected_negative_flag_byte & 0x81).get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test AND Zero Page"

    def test_ZERO_PAGE_X_no_flag(self):
        self.cpu.set_register_A(0x81)
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x0018, Expected_no_flag_byte)
        self.cpu.write_byte(0x0200, AND.ZERO_PAGE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0x13)

        self.cycles = AND.ZERO_PAGE_X.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_no_flag_byte & 0x81).get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test AND Zero Page X"

    def test_ZERO_PAGE_X_zero_flag(self):
        self.cpu.set_register_A(0x81)
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x0018, Expected_zero_flag_byte)
        self.cpu.write_byte(0x0200, AND.ZERO_PAGE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0x13)

        self.cycles = AND.ZERO_PAGE_X.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_zero_flag_byte & 0x81).get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test AND Zero Page X"

    def test_ZERO_PAGE_X_negative_flag(self):
        self.cpu.set_register_A(0x81)
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x0018, Expected_negative_flag_byte)
        self.cpu.write_byte(0x0200, AND.ZERO_PAGE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0x13)

        self.cycles = AND.ZERO_PAGE_X.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_negative_flag_byte & 0x81).get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test AND Zero Page X"

    def test_ABSOLUTE_Y_no_flag(self):
        self.cpu.set_register_A(0x81)
        self.cpu.set_register_Y(0x05)
        self.cpu.write_byte(0x0200, AND.ABSOLUTE_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0xf0)
        self.cpu.write_byte(0x0202, 0x13)
        self.cpu.write_byte(0x13f5, Expected_no_flag_byte)

        self.cycles = AND.ABSOLUTE_Y.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_no_flag_byte & 0x81).get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test AND Absolute Y"

    def test_ABSOLUTE_Y_CROSSED_PAGE_no_flag(self):
        self.cpu.set_register_A(0x81)
        self.cpu.set_register_Y(0x05)
        self.cpu.write_byte(0x0200, AND.ABSOLUTE_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0xff)
        self.cpu.write_byte(0x0202, 0x13)
        self.cpu.write_byte(0x1404, Expected_no_flag_byte)

        self.cycles = AND.ABSOLUTE_Y.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_no_flag_byte & 0x81).get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test AND Absolute Y"

    def test_ABSOLUTE_Y_zero_flag(self):
        self.cpu.set_register_A(0x81)
        self.cpu.set_register_Y(0x05)
        self.cpu.write_byte(0x0200, AND.ABSOLUTE_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0xf0)
        self.cpu.write_byte(0x0202, 0x13)
        self.cpu.write_byte(0x13f5, Expected_zero_flag_byte)

        self.cycles = AND.ABSOLUTE_Y.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_zero_flag_byte & 0x81).get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test AND Absolute Y"

    def test_ABSOLUTE_Y_CROSSED_PAGE_zero_flag(self):
        self.cpu.set_register_A(0x81)
        self.cpu.set_register_Y(0x05)
        self.cpu.write_byte(0x0200, AND.ABSOLUTE_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0xff)
        self.cpu.write_byte(0x0202, 0x13)
        self.cpu.write_byte(0x1404, Expected_zero_flag_byte)

        self.cycles = AND.ABSOLUTE_Y.CYCLES_CROSSED_PAGE
        self.e_reg = 'A'
        self.e_val = Byte(Expected_zero_flag_byte & 0x81).get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test AND Absolute Y"

    def test_ABSOLUTE_Y_negative_flag(self):
        self.cpu.set_register_A(0x81)
        self.cpu.set_register_Y(0x05)
        self.cpu.write_byte(0x0200, AND.ABSOLUTE_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0xf0)
        self.cpu.write_byte(0x0202, 0x13)
        self.cpu.write_byte(0x13f5, Expected_negative_flag_byte)

        self.cycles = AND.ABSOLUTE_Y.CYCLES_CROSSED_PAGE
        self.e_reg = 'A'
        self.e_val = Byte(Expected_negative_flag_byte & 0x81).get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test AND Absolute Y"

    def test_ABSOLUTE_Y_CROSSED_PAGE_negative_flag(self):
        self.cpu.set_register_A(0x81)
        self.cpu.set_register_Y(0x05)
        self.cpu.write_byte(0x0200, AND.ABSOLUTE_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0xff)
        self.cpu.write_byte(0x0202, 0x13)
        self.cpu.write_byte(0x1404, Expected_negative_flag_byte)

        self.cycles = AND.ABSOLUTE_Y.CYCLES_CROSSED_PAGE
        self.e_reg = 'A'
        self.e_val = Byte(Expected_negative_flag_byte & 0x81).get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test AND Absolute Y"

    def test_ABSOLUTE_X_no_flag(self):
        self.cpu.set_register_A(0x81)
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x0200, AND.ABSOLUTE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0xf0)
        self.cpu.write_byte(0x0202, 0x13)
        self.cpu.write_byte(0x13f5, Expected_no_flag_byte)

        self.cycles = AND.ABSOLUTE_X.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_no_flag_byte & 0x81).get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test AND Absolute X"

    def test_ABSOLUTE_X_zero_flag(self):
        self.cpu.set_register_A(0x80)
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x0200, AND.ABSOLUTE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0xf0)
        self.cpu.write_byte(0x0202, 0x13)
        self.cpu.write_byte(0x13f5, Expected_zero_flag_byte)

        self.cycles = AND.ABSOLUTE_X.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_no_flag_byte & 0x80).get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test AND Absolute X"

    def test_ABSOLUTE_X_negative_flag(self):
        self.cpu.set_register_A(0x81)
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x0200, AND.ABSOLUTE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0xf0)
        self.cpu.write_byte(0x0202, 0x13)
        self.cpu.write_byte(0x13f5, Expected_negative_flag_byte)

        self.cycles = AND.ABSOLUTE_X.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_negative_flag_byte & 0x81).get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test AND Absolute X"

    def test_ABSOLUTE_X_CROSSED_PAGE_no_flag(self):
        self.cpu.set_register_A(0x81)
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x0200, AND.ABSOLUTE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0xff)
        self.cpu.write_byte(0x0202, 0x13)
        self.cpu.write_byte(0x1404, Expected_no_flag_byte)

        self.cycles = AND.ABSOLUTE_X.CYCLES_CROSSED_PAGE
        self.e_reg = 'A'
        self.e_val = Byte(Expected_no_flag_byte & 0x81).get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test AND Absolute X"

    def test_ABSOLUTE_X_CROSSED_PAGE_zero_flag(self):
        self.cpu.set_register_A(0x81)
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x0200, AND.ABSOLUTE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0xff)
        self.cpu.write_byte(0x0202, 0x13)
        self.cpu.write_byte(0x1404, Expected_zero_flag_byte)

        self.cycles = AND.ABSOLUTE_X.CYCLES_CROSSED_PAGE
        self.e_reg = 'A'
        self.e_val = Byte(Expected_zero_flag_byte & 0x81).get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test AND Absolute X"

    def test_ABSOLUTE_X_CROSSED_PAGE_negative_flag(self):
        self.cpu.set_register_A(0x81)
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x0200, AND.ABSOLUTE_X.OPCODE)
        self.cpu.write_word(0x0201, 0x13ff)
        self.cpu.write_byte(0x1404, Expected_negative_flag_byte)

        self.cycles = AND.ABSOLUTE_X.CYCLES_CROSSED_PAGE
        self.e_reg = 'A'
        self.e_val = Byte(Expected_negative_flag_byte & 0x81).get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test AND Absolute X"

    def tearDown(self) -> None:
        e, a, m = execute_and_assert(self.cpu, self.cycles, self.e_reg, self.e_val,
                                     self.flags, self.test_name, self.mode)
        self.assertEqual(e, a, m)


class Test_EOR(unittest.TestCase):
    def setUp(self) -> None:
        self.cpu: CPU = T_Reset_cpu()

    def test_INDIRECT_X_no_flag(self):
        self.cpu.set_register_A(0x41)
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x0018, 0xf0)
        self.cpu.write_byte(0x0019, 0x13)
        self.cpu.write_byte(0x0200, EOR.INDIRECT_X.OPCODE)
        self.cpu.write_byte(0x0201, 0x13)
        self.cpu.write_byte(0x13f0, Expected_no_flag_byte)

        self.cycles = EOR.INDIRECT_X.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_no_flag_byte ^ 0x41).get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test EOR Zero Page"

    def test_INDIRECT_X_zero_flag(self):
        self.cpu.set_register_A(0x00)
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x0018, 0xf0)
        self.cpu.write_byte(0x0019, 0x13)
        self.cpu.write_byte(0x0200, EOR.INDIRECT_X.OPCODE)
        self.cpu.write_byte(0x0201, 0x13)
        self.cpu.write_byte(0x13f0, Expected_zero_flag_byte)

        self.cycles = EOR.INDIRECT_X.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_zero_flag_byte ^ 0x00).get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test EOR Zero Page"

    def test_INDIRECT_X_negative_flag(self):
        self.cpu.set_register_A(0x41)
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x0018, 0xf0)
        self.cpu.write_byte(0x0019, 0x13)
        self.cpu.write_byte(0x0200, EOR.INDIRECT_X.OPCODE)
        self.cpu.write_byte(0x0201, 0x13)
        self.cpu.write_byte(0x13f0, Expected_negative_flag_byte)

        self.cycles = EOR.INDIRECT_X.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_negative_flag_byte ^ 0x41).get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test EOR Zero Page"

    def test_ZERO_PAGE_no_flag(self):
        self.cpu.set_register_A(0x41)
        self.cpu.write_byte(0x0013, Expected_no_flag_byte)
        self.cpu.write_byte(0x0200, EOR.ZERO_PAGE.OPCODE)
        self.cpu.write_byte(0x0201, 0x13)

        self.cycles = EOR.ZERO_PAGE.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_no_flag_byte ^ 0x41).get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test EOR Zero Page"

    def test_ZERO_PAGE_zero_flag(self):
        self.cpu.set_register_A(0x00)
        self.cpu.write_byte(0x0013, Expected_zero_flag_byte)
        self.cpu.write_byte(0x0200, EOR.ZERO_PAGE.OPCODE)
        self.cpu.write_byte(0x0201, 0x13)

        self.cycles = EOR.ZERO_PAGE.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_zero_flag_byte ^ 0x00).get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test EOR Zero Page"

    def test_ZERO_PAGE_negative_flag(self):
        self.cpu.set_register_A(0x41)
        self.cpu.write_byte(0x0013, Expected_negative_flag_byte)
        self.cpu.write_byte(0x0200, EOR.ZERO_PAGE.OPCODE)
        self.cpu.write_byte(0x0201, 0x13)

        self.cycles = EOR.ZERO_PAGE.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_negative_flag_byte ^ 0x41).get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test EOR Zero Page"

    def test_IMMEDIATE_no_flag(self):
        self.cpu.set_register_A(0x41)
        self.cpu.write_byte(0x0200, EOR.IMMEDIATE.OPCODE)
        self.cpu.write_byte(0x0201, Expected_no_flag_byte)

        self.cycles = EOR.IMMEDIATE.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_no_flag_byte ^ 0x41).get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test EOR Immediate"

    def test_IMMEDIATE_zero_flag(self):
        self.cpu.set_register_A(0x00)
        self.cpu.write_byte(0x0200, EOR.IMMEDIATE.OPCODE)
        self.cpu.write_byte(0x0201, Expected_zero_flag_byte)

        self.cycles = EOR.IMMEDIATE.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_zero_flag_byte ^ 0x00).get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test EOR Immediate"

    def test_IMMEDIATE_negative_flag(self):
        self.cpu.set_register_A(0x41)
        self.cpu.write_byte(0x0200, EOR.IMMEDIATE.OPCODE)
        self.cpu.write_byte(0x0201, Expected_negative_flag_byte)

        self.cycles = EOR.IMMEDIATE.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_negative_flag_byte ^ 0x41).get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test EOR Immediate"

    def test_ABSOLUTE_no_flag(self):
        self.cpu.set_register_A(0x41)
        self.cpu.write_byte(0x0200, EOR.ABSOLUTE.OPCODE)
        self.cpu.write_byte(0x0201, 0xff)
        self.cpu.write_byte(0x0202, 0x13)
        self.cpu.write_byte(0x13ff, Expected_no_flag_byte)

        self.cycles = EOR.ABSOLUTE.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_no_flag_byte ^ 0x41).get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test EOR Absolute"

    def test_ABSOLUTE_zero_flag(self):
        self.cpu.set_register_A(0x00)
        self.cpu.write_byte(0x0200, EOR.ABSOLUTE.OPCODE)
        self.cpu.write_byte(0x0201, 0xff)
        self.cpu.write_byte(0x0202, 0x13)
        self.cpu.write_byte(0x13ff, Expected_zero_flag_byte)

        self.cycles = EOR.ABSOLUTE.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_zero_flag_byte ^ 0x00).get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test EOR Absolute"

    def test_ABSOLUTE_negative_flag(self):
        self.cpu.set_register_A(0x41)
        self.cpu.write_byte(0x0200, EOR.ABSOLUTE.OPCODE)
        self.cpu.write_byte(0x0201, 0xff)
        self.cpu.write_byte(0x0202, 0x13)
        self.cpu.write_byte(0x13ff, Expected_negative_flag_byte)

        self.cycles = EOR.ABSOLUTE.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_negative_flag_byte ^ 0x41).get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test EOR Absolute"

    def test_INDIRECT_Y_no_flag(self):
        self.cpu.set_register_A(0x41)
        self.cpu.set_register_Y(0x05)
        self.cpu.write_byte(0x0013, 0xf0)
        self.cpu.write_byte(0x0014, 0x13)
        self.cpu.write_byte(0x0200, EOR.INDIRECT_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0x13)
        self.cpu.write_byte(0x13f5, Expected_no_flag_byte)

        self.cycles = EOR.INDIRECT_Y.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_no_flag_byte ^ 0x41).get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test EOR Zero Page"

    def test_INDIRECT_Y_zero_flag(self):
        self.cpu.set_register_A(0x00)
        self.cpu.set_register_Y(0x05)
        self.cpu.write_byte(0x0013, 0xf0)
        self.cpu.write_byte(0x0014, 0x13)
        self.cpu.write_byte(0x0200, EOR.INDIRECT_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0x13)
        self.cpu.write_byte(0x13f5, Expected_zero_flag_byte)

        self.cycles = EOR.INDIRECT_Y.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_zero_flag_byte ^ 0x00).get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test EOR Zero Page"

    def test_INDIRECT_Y_negative_flag(self):
        self.cpu.set_register_A(0x41)
        self.cpu.set_register_Y(0x05)
        self.cpu.write_byte(0x0013, 0xf0)
        self.cpu.write_byte(0x0014, 0x13)
        self.cpu.write_byte(0x0200, EOR.INDIRECT_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0x13)
        self.cpu.write_byte(0x13f5, Expected_negative_flag_byte)

        self.cycles = EOR.INDIRECT_Y.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_negative_flag_byte ^ 0x41).get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test EOR Zero Page"

    def test_INDIRECT_Y_CROSSED_PAGE_no_flag(self):
        self.cpu.set_register_A(0x41)
        self.cpu.set_register_Y(0x05)
        self.cpu.write_byte(0x0013, 0xff)
        self.cpu.write_byte(0x0014, 0x13)
        self.cpu.write_byte(0x0200, EOR.INDIRECT_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0x13)
        self.cpu.write_byte(0x1404, Expected_no_flag_byte)

        self.cycles = EOR.INDIRECT_Y.CYCLES_CROSSED_PAGE
        self.e_reg = 'A'
        self.e_val = Byte(Expected_no_flag_byte ^ 0x41).get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test EOR Zero Page"

    def test_INDIRECT_Y_CROSSED_PAGE_zero_flag(self):
        self.cpu.set_register_A(0x00)
        self.cpu.set_register_Y(0x05)
        self.cpu.write_byte(0x0013, 0xff)
        self.cpu.write_byte(0x0014, 0x13)
        self.cpu.write_byte(0x0200, EOR.INDIRECT_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0x13)
        self.cpu.write_byte(0x1404, Expected_zero_flag_byte)

        self.cycles = EOR.INDIRECT_Y.CYCLES_CROSSED_PAGE
        self.e_reg = 'A'
        self.e_val = Byte(Expected_zero_flag_byte ^ 0x00).get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test EOR Zero Page"

    def test_INDIRECT_Y_CROSSED_PAGE_negative_flag(self):
        self.cpu.set_register_A(0x41)
        self.cpu.set_register_Y(0x05)
        self.cpu.write_byte(0x0013, 0xff)
        self.cpu.write_byte(0x0014, 0x13)
        self.cpu.write_byte(0x0200, EOR.INDIRECT_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0x13)
        self.cpu.write_byte(0x1404, Expected_negative_flag_byte)

        self.cycles = EOR.INDIRECT_Y.CYCLES_CROSSED_PAGE
        self.e_reg = 'A'
        self.e_val = Byte(Expected_negative_flag_byte ^ 0x41).get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test EOR Zero Page"

    def test_ZERO_PAGE_X_no_flag(self):
        self.cpu.set_register_A(0x41)
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x0018, Expected_no_flag_byte)
        self.cpu.write_byte(0x0200, EOR.ZERO_PAGE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0x13)

        self.cycles = EOR.ZERO_PAGE_X.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_no_flag_byte ^ 0x41).get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test EOR Zero Page X"

    def test_ZERO_PAGE_X_zero_flag(self):
        self.cpu.set_register_A(0x00)
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x0018, Expected_zero_flag_byte)
        self.cpu.write_byte(0x0200, EOR.ZERO_PAGE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0x13)

        self.cycles = EOR.ZERO_PAGE_X.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_zero_flag_byte ^ 0x00).get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test EOR Zero Page X"

    def test_ZERO_PAGE_X_negative_flag(self):
        self.cpu.set_register_A(0x41)
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x0018, Expected_negative_flag_byte)
        self.cpu.write_byte(0x0200, EOR.ZERO_PAGE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0x13)

        self.cycles = EOR.ZERO_PAGE_X.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_negative_flag_byte ^ 0x41).get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test EOR Zero Page X"

    def test_ABSOLUTE_Y_no_flag(self):
        self.cpu.set_register_A(0x41)
        self.cpu.set_register_Y(0x05)
        self.cpu.write_byte(0x0200, EOR.ABSOLUTE_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0xf0)
        self.cpu.write_byte(0x0202, 0x13)
        self.cpu.write_byte(0x13f5, Expected_no_flag_byte)

        self.cycles = EOR.ABSOLUTE_Y.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_no_flag_byte ^ 0x41).get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test EOR Absolute Y"

    def test_ABSOLUTE_Y_zero_flag(self):
        self.cpu.set_register_A(0x00)
        self.cpu.set_register_Y(0x05)
        self.cpu.write_byte(0x0200, EOR.ABSOLUTE_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0xf0)
        self.cpu.write_byte(0x0202, 0x13)
        self.cpu.write_byte(0x13f5, Expected_zero_flag_byte)

        self.cycles = EOR.ABSOLUTE_Y.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_zero_flag_byte ^ 0x00).get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test EOR Absolute Y"

    def test_ABSOLUTE_Y_negative_flag(self):
        self.cpu.set_register_A(0x41)
        self.cpu.set_register_Y(0x05)
        self.cpu.write_byte(0x0200, EOR.ABSOLUTE_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0xf0)
        self.cpu.write_byte(0x0202, 0x13)
        self.cpu.write_byte(0x13f5, Expected_negative_flag_byte)

        self.cycles = EOR.ABSOLUTE_Y.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_negative_flag_byte ^ 0x41).get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test EOR Absolute Y"

    def test_ABSOLUTE_Y_CROSSED_PAGE_no_flag(self):
        self.cpu.set_register_A(0x41)
        self.cpu.set_register_Y(0x05)
        self.cpu.write_byte(0x0200, EOR.ABSOLUTE_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0xff)
        self.cpu.write_byte(0x0202, 0x13)
        self.cpu.write_byte(0x1404, Expected_no_flag_byte)

        self.cycles = EOR.ABSOLUTE_Y.CYCLES_CROSSED_PAGE
        self.e_reg = 'A'
        self.e_val = Byte(Expected_no_flag_byte ^ 0x41).get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test EOR Absolute Y"

    def test_ABSOLUTE_Y_CROSSED_PAGE_zero_flag(self):
        self.cpu.set_register_A(0x00)
        self.cpu.set_register_Y(0x05)
        self.cpu.write_byte(0x0200, EOR.ABSOLUTE_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0xff)
        self.cpu.write_byte(0x0202, 0x13)
        self.cpu.write_byte(0x1404, Expected_zero_flag_byte)

        self.cycles = EOR.ABSOLUTE_Y.CYCLES_CROSSED_PAGE
        self.e_reg = 'A'
        self.e_val = Byte(Expected_zero_flag_byte ^ 0x00).get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test EOR Absolute Y"

    def test_ABSOLUTE_Y_CROSSED_PAGE_negative_flag(self):
        self.cpu.set_register_A(0x41)
        self.cpu.set_register_Y(0x05)
        self.cpu.write_byte(0x0200, EOR.ABSOLUTE_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0xff)
        self.cpu.write_byte(0x0202, 0x13)
        self.cpu.write_byte(0x1404, Expected_negative_flag_byte)

        self.cycles = EOR.ABSOLUTE_Y.CYCLES_CROSSED_PAGE
        self.e_reg = 'A'
        self.e_val = Byte(Expected_negative_flag_byte ^ 0x41).get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test EOR Absolute Y"

    def test_ABSOLUTE_X_no_flag(self):
        self.cpu.set_register_A(0x41)
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x0200, EOR.ABSOLUTE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0xf0)
        self.cpu.write_byte(0x0202, 0x13)
        self.cpu.write_byte(0x13f5, Expected_no_flag_byte)

        self.cycles = EOR.ABSOLUTE_X.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_no_flag_byte ^ 0x41).get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test EOR Absolute X"

    def test_ABSOLUTE_X_zero_flag(self):
        self.cpu.set_register_A(0x00)
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x0200, EOR.ABSOLUTE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0xf0)
        self.cpu.write_byte(0x0202, 0x13)
        self.cpu.write_byte(0x13f5, Expected_zero_flag_byte)

        self.cycles = EOR.ABSOLUTE_X.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_zero_flag_byte ^ 0x00).get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test EOR Absolute X"

    def test_ABSOLUTE_X_negative_flag(self):
        self.cpu.set_register_A(0x41)
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x0200, EOR.ABSOLUTE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0xf0)
        self.cpu.write_byte(0x0202, 0x13)
        self.cpu.write_byte(0x13f5, Expected_negative_flag_byte)

        self.cycles = EOR.ABSOLUTE_X.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_negative_flag_byte ^ 0x41).get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test EOR Absolute X"

    def test_ABSOLUTE_X_CROSSED_PAGE_no_flag(self):
        self.cpu.set_register_A(0x41)
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x0200, EOR.ABSOLUTE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0xff)
        self.cpu.write_byte(0x0202, 0x13)
        self.cpu.write_byte(0x1404, Expected_no_flag_byte)

        self.cycles = EOR.ABSOLUTE_X.CYCLES_CROSSED_PAGE
        self.e_reg = 'A'
        self.e_val = Byte(Expected_no_flag_byte ^ 0x41).get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test EOR Absolute X"

    def test_ABSOLUTE_X_CROSSED_PAGE_zero_flag(self):
        self.cpu.set_register_A(0x00)
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x0200, EOR.ABSOLUTE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0xff)
        self.cpu.write_byte(0x0202, 0x13)
        self.cpu.write_byte(0x1404, Expected_zero_flag_byte)

        self.cycles = EOR.ABSOLUTE_X.CYCLES_CROSSED_PAGE
        self.e_reg = 'A'
        self.e_val = Byte(Expected_zero_flag_byte ^ 0x00).get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test EOR Absolute X"

    def test_ABSOLUTE_X_CROSSED_PAGE_negative_flag(self):
        self.cpu.set_register_A(0x41)
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x0200, EOR.ABSOLUTE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0xff)
        self.cpu.write_byte(0x0202, 0x13)
        self.cpu.write_byte(0x1404, Expected_negative_flag_byte)

        self.cycles = EOR.ABSOLUTE_X.CYCLES_CROSSED_PAGE
        self.e_reg = 'A'
        self.e_val = Byte(Expected_negative_flag_byte ^ 0x41).get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test EOR Absolute X"

    def tearDown(self) -> None:
        e, a, m = execute_and_assert(self.cpu, self.cycles, self.e_reg, self.e_val,
                                     self.flags, self.test_name, self.mode)
        self.assertEqual(e, a, m)


class Test_ORA(unittest.TestCase):
    def setUp(self) -> None:
        self.cpu: CPU = T_Reset_cpu()

    def test_INDIRECT_X_no_flag(self):
        self.cpu.set_register_A(0x41)
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x0018, 0xf0)
        self.cpu.write_byte(0x0019, 0x13)
        self.cpu.write_byte(0x0200, ORA.INDIRECT_X.OPCODE)
        self.cpu.write_byte(0x0201, 0x13)
        self.cpu.write_byte(0x13f0, Expected_no_flag_byte)

        self.cycles = ORA.INDIRECT_X.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_no_flag_byte | 0x41).get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ORA Zero Page"

    def test_INDIRECT_X_zero_flag(self):
        self.cpu.set_register_A(0x00)
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x0018, 0xf0)
        self.cpu.write_byte(0x0019, 0x13)
        self.cpu.write_byte(0x0200, ORA.INDIRECT_X.OPCODE)
        self.cpu.write_byte(0x0201, 0x13)
        self.cpu.write_byte(0x13f0, Expected_zero_flag_byte)

        self.cycles = ORA.INDIRECT_X.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_zero_flag_byte | 0x00).get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ORA Zero Page"

    def test_INDIRECT_X_negative_flag(self):
        self.cpu.set_register_A(0x41)
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x0018, 0xf0)
        self.cpu.write_byte(0x0019, 0x13)
        self.cpu.write_byte(0x0200, ORA.INDIRECT_X.OPCODE)
        self.cpu.write_byte(0x0201, 0x13)
        self.cpu.write_byte(0x13f0, Expected_negative_flag_byte)

        self.cycles = ORA.INDIRECT_X.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_negative_flag_byte | 0x41).get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ORA Zero Page"

    def test_ZERO_PAGE_no_flag(self):
        self.cpu.set_register_A(0x41)
        self.cpu.write_byte(0x0013, Expected_no_flag_byte)
        self.cpu.write_byte(0x0200, ORA.ZERO_PAGE.OPCODE)
        self.cpu.write_byte(0x0201, 0x13)

        self.cycles = ORA.ZERO_PAGE.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_no_flag_byte | 0x41).get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ORA Zero Page"

    def test_ZERO_PAGE_zero_flag(self):
        self.cpu.set_register_A(0x00)
        self.cpu.write_byte(0x0013, Expected_zero_flag_byte)
        self.cpu.write_byte(0x0200, ORA.ZERO_PAGE.OPCODE)
        self.cpu.write_byte(0x0201, 0x13)

        self.cycles = ORA.ZERO_PAGE.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_zero_flag_byte | 0x00).get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ORA Zero Page"

    def test_ZERO_PAGE_negative_flag(self):
        self.cpu.set_register_A(0x41)
        self.cpu.write_byte(0x0013, Expected_negative_flag_byte)
        self.cpu.write_byte(0x0200, ORA.ZERO_PAGE.OPCODE)
        self.cpu.write_byte(0x0201, 0x13)

        self.cycles = ORA.ZERO_PAGE.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_negative_flag_byte | 0x41).get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ORA Zero Page"

    def test_IMMEDIATE_no_flag(self):
        self.cpu.set_register_A(0x41)
        self.cpu.write_byte(0x0200, ORA.IMMEDIATE.OPCODE)
        self.cpu.write_byte(0x0201, Expected_no_flag_byte)

        self.cycles = ORA.IMMEDIATE.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_no_flag_byte | 0x41).get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ORA Immediate"

    def test_IMMEDIATE_zero_flag(self):
        self.cpu.set_register_A(0x00)
        self.cpu.write_byte(0x0200, ORA.IMMEDIATE.OPCODE)
        self.cpu.write_byte(0x0201, Expected_zero_flag_byte)

        self.cycles = ORA.IMMEDIATE.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_zero_flag_byte | 0x00).get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ORA Immediate"

    def test_IMMEDIATE_negative_flag(self):
        self.cpu.set_register_A(0x41)
        self.cpu.write_byte(0x0200, ORA.IMMEDIATE.OPCODE)
        self.cpu.write_byte(0x0201, Expected_negative_flag_byte)

        self.cycles = ORA.IMMEDIATE.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_negative_flag_byte | 0x41).get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ORA Immediate"

    def test_ABSOLUTE_no_flag(self):
        self.cpu.set_register_A(0x41)
        self.cpu.write_byte(0x0200, ORA.ABSOLUTE.OPCODE)
        self.cpu.write_byte(0x0201, 0xff)
        self.cpu.write_byte(0x0202, 0x13)
        self.cpu.write_byte(0x13ff, Expected_no_flag_byte)

        self.cycles = ORA.ABSOLUTE.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_no_flag_byte | 0x41).get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ORA Absolute"

    def test_ABSOLUTE_zero_flag(self):
        self.cpu.set_register_A(0x00)
        self.cpu.write_byte(0x0200, ORA.ABSOLUTE.OPCODE)
        self.cpu.write_byte(0x0201, 0xff)
        self.cpu.write_byte(0x0202, 0x13)
        self.cpu.write_byte(0x13ff, Expected_zero_flag_byte)

        self.cycles = ORA.ABSOLUTE.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_zero_flag_byte | 0x00).get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ORA Absolute"

    def test_ABSOLUTE_negative_flag(self):
        self.cpu.set_register_A(0x41)
        self.cpu.write_byte(0x0200, ORA.ABSOLUTE.OPCODE)
        self.cpu.write_byte(0x0201, 0xff)
        self.cpu.write_byte(0x0202, 0x13)
        self.cpu.write_byte(0x13ff, Expected_negative_flag_byte)

        self.cycles = ORA.ABSOLUTE.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_negative_flag_byte | 0x41).get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ORA Absolute"

    def test_INDIRECT_Y_no_flag(self):
        self.cpu.set_register_A(0x41)
        self.cpu.set_register_Y(0x05)
        self.cpu.write_byte(0x0013, 0xf0)
        self.cpu.write_byte(0x0014, 0x13)
        self.cpu.write_byte(0x0200, ORA.INDIRECT_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0x13)
        self.cpu.write_byte(0x13f5, Expected_no_flag_byte)

        self.cycles = ORA.INDIRECT_Y.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_no_flag_byte | 0x41).get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ORA Zero Page"

    def test_INDIRECT_Y_zero_flag(self):
        self.cpu.set_register_A(0x00)
        self.cpu.set_register_Y(0x05)
        self.cpu.write_byte(0x0013, 0xf0)
        self.cpu.write_byte(0x0014, 0x13)
        self.cpu.write_byte(0x0200, ORA.INDIRECT_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0x13)
        self.cpu.write_byte(0x13f5, Expected_zero_flag_byte)

        self.cycles = ORA.INDIRECT_Y.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_zero_flag_byte | 0x00).get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ORA Zero Page"

    def test_INDIRECT_Y_negative_flag(self):
        self.cpu.set_register_A(0x41)
        self.cpu.set_register_Y(0x05)
        self.cpu.write_byte(0x0013, 0xf0)
        self.cpu.write_byte(0x0014, 0x13)
        self.cpu.write_byte(0x0200, ORA.INDIRECT_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0x13)
        self.cpu.write_byte(0x13f5, Expected_negative_flag_byte)

        self.cycles = ORA.INDIRECT_Y.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_negative_flag_byte | 0x41).get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ORA Zero Page"

    def test_INDIRECT_Y_CROSSED_PAGE_no_flag(self):
        self.cpu.set_register_A(0x41)
        self.cpu.set_register_Y(0x05)
        self.cpu.write_byte(0x0013, 0xff)
        self.cpu.write_byte(0x0014, 0x13)
        self.cpu.write_byte(0x0200, ORA.INDIRECT_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0x13)
        self.cpu.write_byte(0x1404, Expected_no_flag_byte)

        self.cycles = ORA.INDIRECT_Y.CYCLES_CROSSED_PAGE
        self.e_reg = 'A'
        self.e_val = Byte(Expected_no_flag_byte | 0x41).get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ORA Zero Page"

    def test_INDIRECT_Y_CROSSED_PAGE_zero_flag(self):
        self.cpu.set_register_A(0x00)
        self.cpu.set_register_Y(0x05)
        self.cpu.write_byte(0x0013, 0xff)
        self.cpu.write_byte(0x0014, 0x13)
        self.cpu.write_byte(0x0200, ORA.INDIRECT_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0x13)
        self.cpu.write_byte(0x1404, Expected_zero_flag_byte)

        self.cycles = ORA.INDIRECT_Y.CYCLES_CROSSED_PAGE
        self.e_reg = 'A'
        self.e_val = Byte(Expected_zero_flag_byte | 0x00).get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ORA Zero Page"

    def test_INDIRECT_Y_CROSSED_PAGE_negative_flag(self):
        self.cpu.set_register_A(0x41)
        self.cpu.set_register_Y(0x05)
        self.cpu.write_byte(0x0013, 0xff)
        self.cpu.write_byte(0x0014, 0x13)
        self.cpu.write_byte(0x0200, ORA.INDIRECT_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0x13)
        self.cpu.write_byte(0x1404, Expected_negative_flag_byte)

        self.cycles = ORA.INDIRECT_Y.CYCLES_CROSSED_PAGE
        self.e_reg = 'A'
        self.e_val = Byte(Expected_negative_flag_byte | 0x41).get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ORA Zero Page"

    def test_ZERO_PAGE_X_no_flag(self):
        self.cpu.set_register_A(0x41)
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x0018, Expected_no_flag_byte)
        self.cpu.write_byte(0x0200, ORA.ZERO_PAGE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0x13)

        self.cycles = ORA.ZERO_PAGE_X.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_no_flag_byte | 0x41).get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ORA Zero Page X"

    def test_ZERO_PAGE_X_zero_flag(self):
        self.cpu.set_register_A(0x00)
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x0018, Expected_zero_flag_byte)
        self.cpu.write_byte(0x0200, ORA.ZERO_PAGE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0x13)

        self.cycles = ORA.ZERO_PAGE_X.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_zero_flag_byte | 0x00).get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ORA Zero Page X"

    def test_ZERO_PAGE_X_negative_flag(self):
        self.cpu.set_register_A(0x41)
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x0018, Expected_negative_flag_byte)
        self.cpu.write_byte(0x0200, ORA.ZERO_PAGE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0x13)

        self.cycles = ORA.ZERO_PAGE_X.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_negative_flag_byte | 0x41).get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ORA Zero Page X"

    def test_ABSOLUTE_Y_no_flag(self):
        self.cpu.set_register_A(0x41)
        self.cpu.set_register_Y(0x05)
        self.cpu.write_byte(0x0200, ORA.ABSOLUTE_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0xf0)
        self.cpu.write_byte(0x0202, 0x13)
        self.cpu.write_byte(0x13f5, Expected_no_flag_byte)

        self.cycles = ORA.ABSOLUTE_Y.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_no_flag_byte | 0x41).get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ORA Absolute Y"

    def test_ABSOLUTE_Y_zero_flag(self):
        self.cpu.set_register_A(0x00)
        self.cpu.set_register_Y(0x05)
        self.cpu.write_byte(0x0200, ORA.ABSOLUTE_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0xf0)
        self.cpu.write_byte(0x0202, 0x13)
        self.cpu.write_byte(0x13f5, Expected_zero_flag_byte)

        self.cycles = ORA.ABSOLUTE_Y.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_zero_flag_byte | 0x00).get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ORA Absolute Y"

    def test_ABSOLUTE_Y_negative_flag(self):
        self.cpu.set_register_A(0x41)
        self.cpu.set_register_Y(0x05)
        self.cpu.write_byte(0x0200, ORA.ABSOLUTE_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0xf0)
        self.cpu.write_byte(0x0202, 0x13)
        self.cpu.write_byte(0x13f5, Expected_negative_flag_byte)

        self.cycles = ORA.ABSOLUTE_Y.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_negative_flag_byte | 0x41).get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ORA Absolute Y"

    def test_ABSOLUTE_Y_CROSSED_PAGE_no_flag(self):
        self.cpu.set_register_A(0x41)
        self.cpu.set_register_Y(0x05)
        self.cpu.write_byte(0x0200, ORA.ABSOLUTE_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0xff)
        self.cpu.write_byte(0x0202, 0x13)
        self.cpu.write_byte(0x1404, Expected_no_flag_byte)

        self.cycles = ORA.ABSOLUTE_Y.CYCLES_CROSSED_PAGE
        self.e_reg = 'A'
        self.e_val = Byte(Expected_no_flag_byte | 0x41).get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ORA Absolute Y"

    def test_ABSOLUTE_Y_CROSSED_PAGE_zero_flag(self):
        self.cpu.set_register_A(0x00)
        self.cpu.set_register_Y(0x05)
        self.cpu.write_byte(0x0200, ORA.ABSOLUTE_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0xff)
        self.cpu.write_byte(0x0202, 0x13)
        self.cpu.write_byte(0x1404, Expected_zero_flag_byte)

        self.cycles = ORA.ABSOLUTE_Y.CYCLES_CROSSED_PAGE
        self.e_reg = 'A'
        self.e_val = Byte(Expected_zero_flag_byte | 0x00).get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ORA Absolute Y"

    def test_ABSOLUTE_Y_CROSSED_PAGE_negative_flag(self):
        self.cpu.set_register_A(0x41)
        self.cpu.set_register_Y(0x05)
        self.cpu.write_byte(0x0200, ORA.ABSOLUTE_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0xff)
        self.cpu.write_byte(0x0202, 0x13)
        self.cpu.write_byte(0x1404, Expected_negative_flag_byte)

        self.cycles = ORA.ABSOLUTE_Y.CYCLES_CROSSED_PAGE
        self.e_reg = 'A'
        self.e_val = Byte(Expected_negative_flag_byte | 0x41).get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ORA Absolute Y"

    def test_ABSOLUTE_X_no_flag(self):
        self.cpu.set_register_A(0x41)
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x0200, ORA.ABSOLUTE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0xf0)
        self.cpu.write_byte(0x0202, 0x13)
        self.cpu.write_byte(0x13f5, Expected_no_flag_byte)

        self.cycles = ORA.ABSOLUTE_X.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_no_flag_byte | 0x41).get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ORA Absolute X"

    def test_ABSOLUTE_X_zero_flag(self):
        self.cpu.set_register_A(0x00)
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x0200, ORA.ABSOLUTE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0xf0)
        self.cpu.write_byte(0x0202, 0x13)
        self.cpu.write_byte(0x13f5, Expected_zero_flag_byte)

        self.cycles = ORA.ABSOLUTE_X.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_zero_flag_byte | 0x00).get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ORA Absolute X"

    def test_ABSOLUTE_X_negative_flag(self):
        self.cpu.set_register_A(0x41)
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x0200, ORA.ABSOLUTE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0xf0)
        self.cpu.write_byte(0x0202, 0x13)
        self.cpu.write_byte(0x13f5, Expected_negative_flag_byte)

        self.cycles = ORA.ABSOLUTE_X.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_negative_flag_byte | 0x41).get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ORA Absolute X"

    def test_ABSOLUTE_X_CROSSED_PAGE_no_flag(self):
        self.cpu.set_register_A(0x41)
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x0200, ORA.ABSOLUTE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0xff)
        self.cpu.write_byte(0x0202, 0x13)
        self.cpu.write_byte(0x1404, Expected_no_flag_byte)

        self.cycles = ORA.ABSOLUTE_X.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_no_flag_byte | 0x41).get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ORA Absolute X"

    def test_ABSOLUTE_X_CROSSED_PAGE_zero_flag(self):
        self.cpu.set_register_A(0x00)
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x0200, ORA.ABSOLUTE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0xff)
        self.cpu.write_byte(0x0202, 0x13)
        self.cpu.write_byte(0x1404, Expected_zero_flag_byte)

        self.cycles = ORA.ABSOLUTE_X.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_zero_flag_byte | 0x00).get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ORA Absolute X"

    def test_ABSOLUTE_X_CROSSED_PAGE_negative_flag(self):
        self.cpu.set_register_A(0x41)
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x0200, ORA.ABSOLUTE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0xff)
        self.cpu.write_byte(0x0202, 0x13)
        self.cpu.write_byte(0x1404, Expected_negative_flag_byte)

        self.cycles = ORA.ABSOLUTE_X.CYCLES
        self.e_reg = 'A'
        self.e_val = Byte(Expected_negative_flag_byte | 0x41).get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test ORA Absolute X"

    def tearDown(self) -> None:
        e, a, m = execute_and_assert(self.cpu, self.cycles, self.e_reg, self.e_val,
                                     self.flags, self.test_name, self.mode)
        self.assertEqual(e, a, m)


class Test_BIT_ZERO_PAGE(unittest.TestCase):
    def setUp(self) -> None:
        self.cpu = T_Reset_cpu()
        self.cpu.write_byte(0x0200, BIT.ZERO_PAGE.OPCODE)
        self.cpu.write_byte(0x0201, 0x30)

    def test_ZERO_PAGE_zvn(self):
        self.cpu.set_register_A(0x0f)
        self.cpu.write_byte(0x0030, 0x08)
        self.Z = 0
        self.V = 0
        self.N = 0
        self.e = 0x0f

    def test_ZERO_PAGE_zvN(self):
        self.cpu.set_register_A(0x80)
        self.cpu.write_byte(0x0030, 0x80)
        self.Z = 0
        self.V = 0
        self.N = 1
        self.e = 0x80

    def test_ZERO_PAGE_zVn(self):
        self.cpu.set_register_A(0x70)
        self.cpu.write_byte(0x0030, 0x70)
        self.Z = 0
        self.V = 1
        self.N = 0
        self.e = 0x70

    def test_ZERO_PAGE_zVN(self):
        self.cpu.set_register_A(0xd0)
        self.cpu.write_byte(0x0030, 0xd0)
        self.Z = 0
        self.V = 1
        self.N = 1
        self.e = 0xd0

    def test_ZERO_PAGE_Zvn(self):
        self.cpu.set_register_A(0xcc)
        self.cpu.write_byte(0x0030, 0x33)
        self.Z = 1
        self.V = 0
        self.N = 0
        self.e = 0xcc

    def test_ZERO_PAGE_ZvN(self):
        self.cpu.set_register_A(0x00)
        self.cpu.write_byte(0x0030, 0x80)
        self.Z = 1
        self.V = 0
        self.N = 1
        self.e = 0x00

    def test_ZERO_PAGE_ZVn(self):
        self.cpu.set_register_A(0x00)
        self.cpu.write_byte(0x0030, 0x70)
        self.Z = 1
        self.V = 1
        self.N = 0
        self.e = 0x00

    def test_ZERO_PAGE_ZVN(self):
        self.cpu.set_register_A(0x00)
        self.cpu.write_byte(0x0030, 0xd0)
        self.Z = 1
        self.V = 1
        self.N = 1
        self.e = 0x00

    def tearDown(self) -> None:
        self.cpu.execute(BIT.ZERO_PAGE.CYCLES)

        test_name = "Test BIT Zero Page"
        flags = self.cpu.get_register_F()

        self.assertEqual(Byte(self.e).get_hex_value(), self.cpu.get_register_A().get_hex_value(),
                         f"{test_name}, Register A value incorrect")

        self.assertEqual(0, self.cpu.cycles,
                         f"{test_name}, CPU Cycles incorrect")

        for i in range(8):
            if i == 0:
                self.assertEqual(self.N, self.cpu.get_register_F().get_bit(i),
                                 f"{test_name}, Flag on position {7 - i} incorrect")
            elif i == 1:
                self.assertEqual(self.V, self.cpu.get_register_F().get_bit(i),
                                 f"{test_name}, Flag on position {7 - i} incorrect")
            elif i == 6:
                self.assertEqual(self.Z, self.cpu.get_register_F().get_bit(i),
                                 f"{test_name}, Flag on position {7 - i} incorrect")
            else:
                self.assertEqual(flags.get_bit(i), self.cpu.get_register_F().get_bit(i),
                                 f"{test_name}, Flag on position {7 - i} incorrect")


class Test_BIT_ABSOLUTE(unittest.TestCase):
    def setUp(self) -> None:
        self.cpu = T_Reset_cpu()
        self.cpu.write_byte(0x0200, BIT.ABSOLUTE.OPCODE)
        self.cpu.write_byte(0x0201, 0xff)
        self.cpu.write_byte(0x0202, 0x13)

    def test_ABSOLUTE_zvn(self):
        self.cpu.set_register_A(0x0f)
        self.cpu.write_byte(0x13ff, 0x08)
        self.Z = 0
        self.V = 0
        self.N = 0
        self.e = 0x0f

    def test_ABSOLUTE_zvN(self):
        self.cpu.set_register_A(0x80)
        self.cpu.write_byte(0x13ff, 0x80)
        self.Z = 0
        self.V = 0
        self.N = 1
        self.e = 0x80

    def test_ABSOLUTE_zVn(self):
        self.cpu.set_register_A(0x70)
        self.cpu.write_byte(0x13ff, 0x70)
        self.Z = 0
        self.V = 1
        self.N = 0
        self.e = 0x70

    def test_ABSOLUTE_zVN(self):
        self.cpu.set_register_A(0xd0)
        self.cpu.write_byte(0x13ff, 0xd0)
        self.Z = 0
        self.V = 1
        self.N = 1
        self.e = 0xd0

    def test_ABSOLUTE_Zvn(self):
        self.cpu.set_register_A(0xcc)
        self.cpu.write_byte(0x13ff, 0x33)
        self.Z = 1
        self.V = 0
        self.N = 0
        self.e = 0xcc

    def test_ABSOLUTE_ZvN(self):
        self.cpu.set_register_A(0x00)
        self.cpu.write_byte(0x13ff, 0x80)
        self.Z = 1
        self.V = 0
        self.N = 1
        self.e = 0x00

    def test_ABSOLUTE_ZVn(self):
        self.cpu.set_register_A(0x00)
        self.cpu.write_byte(0x13ff, 0x70)
        self.Z = 1
        self.V = 1
        self.N = 0
        self.e = 0x00

    def test_ABSOLUTE_ZVN(self):
        self.cpu.set_register_A(0x00)
        self.cpu.write_byte(0x13ff, 0xd0)
        self.Z = 1
        self.V = 1
        self.N = 1
        self.e = 0x00

    def tearDown(self) -> None:
        self.cpu.execute(BIT.ABSOLUTE.CYCLES)

        test_name = "Test BIT Absolute"
        flags = self.cpu.get_register_F()

        self.assertEqual(Byte(self.e).get_hex_value(), self.cpu.get_register_A().get_hex_value(),
                         f"{test_name}, Register A value incorrect")

        self.assertEqual(0, self.cpu.cycles,
                         f"{test_name}, CPU Cycles incorrect")

        for i in range(8):
            if i == 0:
                self.assertEqual(self.N, self.cpu.get_register_F().get_bit(i),
                                 f"{test_name}, Flag on position {7 - i} incorrect")
            elif i == 1:
                self.assertEqual(self.V, self.cpu.get_register_F().get_bit(i),
                                 f"{test_name}, Flag on position {7 - i} incorrect")
            elif i == 6:
                self.assertEqual(self.Z, self.cpu.get_register_F().get_bit(i),
                                 f"{test_name}, Flag on position {7 - i} incorrect")
            else:
                self.assertEqual(flags.get_bit(i), self.cpu.get_register_F().get_bit(i),
                                 f"{test_name}, Flag on position {7 - i} incorrect")


if __name__ == '__main__':
    unittest.main()
