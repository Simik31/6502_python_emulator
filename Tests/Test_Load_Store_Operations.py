# ##############################
#  Copyright (c) 2021          #
#                              #
#  Author: Martin Šimara       #
#  Last modified on 12.2.2021  #
# ##############################

import unittest
from CPU import CPU
from Instructions.Load_Store_Operations import LDA, LDX, LDY, STA, STX, STY
from Testing_constants import T_Reset_cpu, execute_and_assert
from Testing_constants import Expected_no_flag_byte, Expected_zero_flag_byte, Expected_negative_flag_byte


class Test_LDA(unittest.TestCase):
    def setUp(self) -> None:
        self.cpu: CPU = T_Reset_cpu()

    def test_INDIRECT_X_no_flag(self):
        # using cpu method to ensure that Register X contains correct data (LDX may not be working correctly)
        self.cpu.set_register_X(0x04)

        self.cpu.write_byte(0x0200, LDA.INDIRECT_X.OPCODE)
        self.cpu.write_byte(0x0201, 0x02)
        self.cpu.write_byte(0x0006, 0x00)
        self.cpu.write_byte(0x0007, 0x80)
        self.cpu.write_byte(0x8000, Expected_no_flag_byte)

        self.cycles = LDA.INDIRECT_X.CYCLES
        self.e_reg = 'A'
        self.e_val = Expected_no_flag_byte.get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F().copy()
        self.test_name = "Test LDA Indirect X"

    def test_INDIRECT_X_zero_flag(self):
        # using cpu method to ensure that Register X contains correct data (LDX may not be working correctly)
        self.cpu.set_register_X(0x04)

        self.cpu.write_byte(0x0200, LDA.INDIRECT_X.OPCODE)
        self.cpu.write_byte(0x0201, 0x02)
        self.cpu.write_byte(0x0006, 0x00)
        self.cpu.write_byte(0x0007, 0x00)
        self.cpu.write_byte(0x8000, Expected_zero_flag_byte)

        self.cycles = LDA.INDIRECT_X.CYCLES
        self.e_reg = 'A'
        self.e_val = Expected_zero_flag_byte.get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F().copy()
        self.test_name = "Test LDA Indirect X"

    def test_INDIRECT_X_negative_flag(self):
        # using cpu method to ensure that Register X contains correct data (LDX may not be working correctly)
        self.cpu.set_register_X(0x04)

        self.cpu.write_byte(0x0200, LDA.INDIRECT_X.OPCODE)
        self.cpu.write_byte(0x0201, 0x02)
        self.cpu.write_byte(0x0006, 0x00)
        self.cpu.write_byte(0x0007, 0x80)
        self.cpu.write_byte(0x8000, Expected_negative_flag_byte)

        self.cycles = LDA.INDIRECT_X.CYCLES
        self.e_reg = 'A'
        self.e_val = Expected_negative_flag_byte.get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F().copy()
        self.test_name = "Test LDA Indirect X"

    def test_ZERO_PAGE_no_flags(self):
        self.cpu.write_byte(0x0200, LDA.ZERO_PAGE.OPCODE)
        self.cpu.write_byte(0x0201, 0x31)
        self.cpu.write_byte(0x0031, Expected_no_flag_byte)

        self.cycles = LDA.ZERO_PAGE.CYCLES
        self.e_reg = 'A'
        self.e_val = Expected_no_flag_byte.get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F().copy()
        self.test_name = "Test LDA Zero Page"

    def test_ZERO_PAGE_zero_flags(self):
        self.cpu.write_byte(0x0200, LDA.ZERO_PAGE.OPCODE)
        self.cpu.write_byte(0x0201, 0x31)
        self.cpu.write_byte(0x0031, Expected_zero_flag_byte)

        self.cycles = LDA.ZERO_PAGE.CYCLES
        self.e_reg = 'A'
        self.e_val = Expected_zero_flag_byte.get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F().copy()
        self.test_name = "Test LDA Zero Page"

    def test_ZERO_PAGE_negative_flags(self):
        self.cpu.write_byte(0x0200, LDA.ZERO_PAGE.OPCODE)
        self.cpu.write_byte(0x0201, 0x31)
        self.cpu.write_byte(0x0031, Expected_negative_flag_byte)

        self.cycles = LDA.ZERO_PAGE.CYCLES
        self.e_reg = 'A'
        self.e_val = Expected_negative_flag_byte.get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F().copy()
        self.test_name = "Test LDA Zero Page"

    def test_IMMEDIATE_no_flags(self):
        self.cpu.write_byte(0x0200, LDA.IMMEDIATE.OPCODE)
        self.cpu.write_byte(0x0201, Expected_no_flag_byte)

        self.cycles = LDA.IMMEDIATE.CYCLES
        self.e_reg = 'A'
        self.e_val = Expected_no_flag_byte.get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F().copy()
        self.test_name = "Test LDA Immediate"

    def test_IMMEDIATE_zero_flag(self):
        self.cpu.write_byte(0x0200, LDA.IMMEDIATE.OPCODE)
        self.cpu.write_byte(0x0201, Expected_zero_flag_byte)

        self.cycles = LDA.IMMEDIATE.CYCLES
        self.e_reg = 'A'
        self.e_val = Expected_zero_flag_byte.get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F().copy()
        self.test_name = "Test LDA Immediate"

    def test_IMMEDIATE_negative_flag(self):
        self.cpu.write_byte(0x0200, LDA.IMMEDIATE.OPCODE)
        self.cpu.write_byte(0x0201, Expected_negative_flag_byte)

        self.cycles = LDA.IMMEDIATE.CYCLES
        self.e_reg = 'A'
        self.e_val = Expected_negative_flag_byte.get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F().copy()
        self.test_name = "Test LDA Immediate"

    def test_ABSOLUTE_no_flag(self):
        self.cpu.write_byte(0x0200, LDA.ABSOLUTE.OPCODE)
        self.cpu.write_byte(0x0201, 0x31)
        self.cpu.write_byte(0x0202, 0xf0)
        self.cpu.write_byte(0xf031, Expected_no_flag_byte)

        self.cycles = LDA.ABSOLUTE.CYCLES
        self.e_reg = 'A'
        self.e_val = Expected_no_flag_byte.get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test LDA Absolute"

    def test_ABSOLUTE_zero_flag(self):
        self.cpu.write_byte(0x0200, LDA.ABSOLUTE.OPCODE)
        self.cpu.write_byte(0x0201, 0x31)
        self.cpu.write_byte(0x0202, 0xf0)
        self.cpu.write_byte(0xf031, Expected_zero_flag_byte)

        self.cycles = LDA.ABSOLUTE.CYCLES
        self.e_reg = 'A'
        self.e_val = Expected_zero_flag_byte.get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test LDA Absolute"

    def test_ABSOLUTE_negative_flag(self):
        self.cpu.write_byte(0x0200, LDA.ABSOLUTE.OPCODE)
        self.cpu.write_byte(0x0201, 0x31)
        self.cpu.write_byte(0x0202, 0xf0)
        self.cpu.write_byte(0xf031, Expected_negative_flag_byte)

        self.cycles = LDA.ABSOLUTE.CYCLES
        self.e_reg = 'A'
        self.e_val = Expected_negative_flag_byte.get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test LDA Absolute"

    def test_INDIRECT_Y_no_flag(self):
        # using cpu method to ensure that Register Y contains correct data (LDY may not be working correctly)
        self.cpu.set_register_Y(0x04)

        self.cpu.write_byte(0x0200, LDA.INDIRECT_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0x02)
        self.cpu.write_byte(0x0002, 0x00)
        self.cpu.write_byte(0x0003, 0x80)
        self.cpu.write_byte(0x8004, Expected_no_flag_byte)

        self.cycles = LDA.INDIRECT_Y.CYCLES
        self.e_reg = 'A'
        self.e_val = Expected_no_flag_byte.get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test LDA Indirect Y"

    def test_INDIRECT_Y_zero_flag(self):
        # using cpu method to ensure that Register Y contains correct data (LDY may not be working correctly)
        self.cpu.set_register_Y(0x04)

        self.cpu.write_byte(0x0200, LDA.INDIRECT_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0x02)
        self.cpu.write_byte(0x0002, 0x00)
        self.cpu.write_byte(0x0003, 0x80)
        self.cpu.write_byte(0x8004, Expected_zero_flag_byte)

        self.cycles = LDA.INDIRECT_Y.CYCLES
        self.e_reg = 'A'
        self.e_val = Expected_zero_flag_byte.get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test LDA Indirect Y"

    def test_INDIRECT_Y_negative_flag(self):
        # using cpu method to ensure that Register Y contains correct data (LDY may not be working correctly)
        self.cpu.set_register_Y(0x04)

        self.cpu.write_byte(0x0200, LDA.INDIRECT_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0x02)
        self.cpu.write_byte(0x0002, 0x00)
        self.cpu.write_byte(0x0003, 0x80)
        self.cpu.write_byte(0x8004, Expected_negative_flag_byte)

        self.cycles = LDA.INDIRECT_Y.CYCLES
        self.e_reg = 'A'
        self.e_val = Expected_negative_flag_byte.get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test LDA Indirect Y"

    def test_INDIRECT_Y_CROSSED_PAGE_no_flag(self):
        # using cpu method to ensure that Register Y contains correct data (LDY may not be working correctly)
        self.cpu.set_register_Y(0x04)

        self.cpu.write_byte(0x0200, LDA.INDIRECT_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0x02)
        self.cpu.write_byte(0x0002, 0xff)
        self.cpu.write_byte(0x0003, 0x80)
        self.cpu.write_byte(0x8103, Expected_no_flag_byte)

        self.cycles = LDA.INDIRECT_Y.CYCLES_CROSSED_PAGE
        self.e_reg = 'A'
        self.e_val = Expected_no_flag_byte.get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test LDA Indirect Y (page crossed)"

    def test_INDIRECT_Y_CROSSED_PAGE_zero_flag(self):
        # using cpu method to ensure that Register Y contains correct data (LDY may not be working correctly)
        self.cpu.set_register_Y(0x04)

        self.cpu.write_byte(0x0200, LDA.INDIRECT_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0x02)
        self.cpu.write_byte(0x0002, 0xff)
        self.cpu.write_byte(0x0003, 0x80)
        self.cpu.write_byte(0x8103, Expected_zero_flag_byte)

        self.cycles = LDA.INDIRECT_Y.CYCLES_CROSSED_PAGE
        self.e_reg = 'A'
        self.e_val = Expected_zero_flag_byte.get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test LDA Indirect Y (page crossed)"

    def test_INDIRECT_Y_CROSSED_PAGE_negative_flag(self):
        # using cpu method to ensure that Register Y contains correct data (LDY may not be working correctly)
        self.cpu.set_register_Y(0x04)

        self.cpu.write_byte(0x0200, LDA.INDIRECT_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0x02)
        self.cpu.write_byte(0x0002, 0xff)
        self.cpu.write_byte(0x0003, 0x80)
        self.cpu.write_byte(0x8103, Expected_negative_flag_byte)

        self.cycles = LDA.INDIRECT_Y.CYCLES_CROSSED_PAGE
        self.e_reg = 'A'
        self.e_val = Expected_negative_flag_byte.get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test LDA Indirect Y (page crossed)"

    def test_ZERO_PAGE_X_no_flags(self):
        # using cpu method to ensure that Register X contains correct data (LDX may not be working correctly)
        self.cpu.set_register_X(0x05)

        self.cpu.write_byte(0x0200, LDA.ZERO_PAGE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0x31)
        self.cpu.write_byte(0x0036, Expected_no_flag_byte)

        self.cycles = LDA.ZERO_PAGE_X.CYCLES
        self.e_reg = 'A'
        self.e_val = Expected_no_flag_byte.get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test LDA Zero Page X"

    def test_ZERO_PAGE_X_zero_flag(self):
        # using cpu method to ensure that Register X contains correct data (LDX may not be working correctly)
        self.cpu.set_register_X(0x05)

        self.cpu.write_byte(0x0200, LDA.ZERO_PAGE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0x31)
        self.cpu.write_byte(0x0036, Expected_zero_flag_byte)

        self.cycles = LDA.ZERO_PAGE_X.CYCLES
        self.e_reg = 'A'
        self.e_val = Expected_zero_flag_byte.get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test LDA Zero Page X"

    def test_ZERO_PAGE_X_negative_flag(self):
        # using cpu method to ensure that Register X contains correct data (LDX may not be working correctly)
        self.cpu.set_register_X(0x05)

        self.cpu.write_byte(0x0200, LDA.ZERO_PAGE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0x31)
        self.cpu.write_byte(0x0036, Expected_negative_flag_byte)

        self.cycles = LDA.ZERO_PAGE_X.CYCLES
        self.e_reg = 'A'
        self.e_val = Expected_negative_flag_byte.get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test LDA Zero Page X"

    def test_ABSOLUTE_Y_no_flag(self):
        # using cpu method to ensure that Register Y contains correct data (LDY may not be working correctly)
        self.cpu.set_register_Y(0x92)

        self.cpu.write_byte(0x0200, LDA.ABSOLUTE_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0x00)
        self.cpu.write_byte(0x0202, 0x20)
        self.cpu.write_byte(0x2092, Expected_no_flag_byte)

        self.cycles = LDA.ABSOLUTE_Y.CYCLES
        self.e_reg = 'A'
        self.e_val = Expected_no_flag_byte.get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test LDA Absolute Y"

    def test_ABSOLUTE_Y_zero_flag(self):
        # using cpu method to ensure that Register Y contains correct data (LDY may not be working correctly)
        self.cpu.set_register_Y(0x92)

        self.cpu.write_byte(0x0200, LDA.ABSOLUTE_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0x00)
        self.cpu.write_byte(0x0202, 0x20)
        self.cpu.write_byte(0x2092, Expected_zero_flag_byte)

        self.cycles = LDA.ABSOLUTE_Y.CYCLES
        self.e_reg = 'A'
        self.e_val = Expected_zero_flag_byte.get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test LDA Absolute Y"

    def test_ABSOLUTE_Y_negative_flag(self):
        # using cpu method to ensure that Register Y contains correct data (LDY may not be working correctly)
        self.cpu.set_register_Y(0x92)

        self.cpu.write_byte(0x0200, LDA.ABSOLUTE_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0x00)
        self.cpu.write_byte(0x0202, 0x20)
        self.cpu.write_byte(0x2092, Expected_negative_flag_byte)

        self.cycles = LDA.ABSOLUTE_Y.CYCLES
        self.e_reg = 'A'
        self.e_val = Expected_negative_flag_byte.get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test LDA Absolute Y"

    def test_ABSOLUTE_Y_CROSSED_PAGE_no_flag(self):
        # using cpu method to ensure that Register Y contains correct data (LDY may not be working correctly)
        self.cpu.set_register_Y(0x92)

        self.cpu.write_byte(0x0200, LDA.ABSOLUTE_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0x6f)
        self.cpu.write_byte(0x0202, 0x20)
        self.cpu.write_byte(0x2101, Expected_no_flag_byte)

        self.cycles = LDA.ABSOLUTE_Y.CYCLES_CROSSED_PAGE
        self.e_reg = 'A'
        self.e_val = Expected_no_flag_byte.get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test LDA Absolute Y (crossed page)"

    def test_ABSOLUTE_Y_CROSSED_PAGE_zero_flag(self):
        # using cpu method to ensure that Register Y contains correct data (LDY may not be working correctly)
        self.cpu.set_register_Y(0x92)

        self.cpu.write_byte(0x0200, LDA.ABSOLUTE_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0x6f)
        self.cpu.write_byte(0x0202, 0x20)
        self.cpu.write_byte(0x2101, Expected_zero_flag_byte)

        self.cycles = LDA.ABSOLUTE_Y.CYCLES_CROSSED_PAGE
        self.e_reg = 'A'
        self.e_val = Expected_zero_flag_byte.get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test LDA Absolute Y (crossed page)"

    def test_ABSOLUTE_Y_CROSSED_PAGE_negative_flag(self):
        # using cpu method to ensure that Register Y contains correct data (LDY may not be working correctly)
        self.cpu.set_register_Y(0x92)

        self.cpu.write_byte(0x0200, LDA.ABSOLUTE_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0x6f)
        self.cpu.write_byte(0x0202, 0x20)
        self.cpu.write_byte(0x2101, Expected_negative_flag_byte)

        self.cycles = LDA.ABSOLUTE_Y.CYCLES_CROSSED_PAGE
        self.e_reg = 'A'
        self.e_val = Expected_negative_flag_byte.get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test LDA Absolute Y (crossed page)"

    def test_ABSOLUTE_X_no_flag(self):
        # using cpu method to ensure that Register X contains correct data (LDX may not be working correctly)
        self.cpu.set_register_X(0x92)

        self.cpu.write_byte(0x0200, LDA.ABSOLUTE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0x00)
        self.cpu.write_byte(0x0202, 0x20)
        self.cpu.write_byte(0x2092, Expected_no_flag_byte)

        self.cycles = LDA.ABSOLUTE_X.CYCLES
        self.e_reg = 'A'
        self.e_val = Expected_no_flag_byte.get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test LDA Absolute X"

    def test_ABSOLUTE_X_zero_flag(self):
        # using cpu method to ensure that Register X contains correct data (LDX may not be working correctly)
        self.cpu.set_register_X(0x92)

        self.cpu.write_byte(0x0200, LDA.ABSOLUTE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0x00)
        self.cpu.write_byte(0x0202, 0x20)
        self.cpu.write_byte(0x2092, Expected_zero_flag_byte)

        self.cycles = LDA.ABSOLUTE_X.CYCLES
        self.e_reg = 'A'
        self.e_val = Expected_zero_flag_byte.get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test LDA Absolute X"

    def test_ABSOLUTE_X_negative_flag(self):
        # using cpu method to ensure that Register X contains correct data (LDX may not be working correctly)
        self.cpu.set_register_X(0x92)

        self.cpu.write_byte(0x0200, LDA.ABSOLUTE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0x00)
        self.cpu.write_byte(0x0202, 0x20)
        self.cpu.write_byte(0x2092, Expected_negative_flag_byte)

        self.cycles = LDA.ABSOLUTE_X.CYCLES
        self.e_reg = 'A'
        self.e_val = Expected_negative_flag_byte.get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test LDA Absolute X"

    def test_ABSOLUTE_X_CROSSED_PAGE_no_flag(self):
        # using cpu method to ensure that Register X contains correct data (LDX may not be working correctly)
        self.cpu.set_register_X(0x92)

        self.cpu.write_byte(0x0200, LDA.ABSOLUTE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0x6f)
        self.cpu.write_byte(0x0202, 0x20)
        self.cpu.write_byte(0x2101, Expected_no_flag_byte)

        self.cycles = LDA.ABSOLUTE_X.CYCLES_CROSSED_PAGE
        self.e_reg = 'A'
        self.e_val = Expected_no_flag_byte.get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test LDA Absolute X (crossed page)"

    def test_ABSOLUTE_X_CROSSED_PAGE_zero_flag(self):
        # using cpu method to ensure that Register X contains correct data (LDX may not be working correctly)
        self.cpu.set_register_X(0x92)

        self.cpu.write_byte(0x0200, LDA.ABSOLUTE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0x6f)
        self.cpu.write_byte(0x0202, 0x20)
        self.cpu.write_byte(0x2101, Expected_zero_flag_byte)

        self.cycles = LDA.ABSOLUTE_X.CYCLES_CROSSED_PAGE
        self.e_reg = 'A'
        self.e_val = Expected_zero_flag_byte.get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test LDA Absolute X (crossed page)"

    def test_ABSOLUTE_X_CROSSED_PAGE_negative_flag(self):
        # using cpu method to ensure that Register X contains correct data (LDX may not be working correctly)
        self.cpu.set_register_X(0x92)

        self.cpu.write_byte(0x0200, LDA.ABSOLUTE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0x6f)
        self.cpu.write_byte(0x0202, 0x20)
        self.cpu.write_byte(0x2101, Expected_negative_flag_byte)

        self.cycles = LDA.ABSOLUTE_X.CYCLES_CROSSED_PAGE
        self.e_reg = 'A'
        self.e_val = Expected_negative_flag_byte.get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test LDA Absolute X (crossed page)"

    def tearDown(self) -> None:
        e, a, m = execute_and_assert(self.cpu, self.cycles, self.e_reg, self.e_val,
                                     self.flags, self.test_name, self.mode)
        self.assertEqual(e, a, m)


class Test_LDX(unittest.TestCase):
    def setUp(self) -> None:
        self.cpu: CPU = T_Reset_cpu()

    def test_IMMEDIATE_no_flags(self):
        self.cpu.write_byte(0x0200, LDX.IMMEDIATE.OPCODE)
        self.cpu.write_byte(0x0201, Expected_no_flag_byte)

        self.cycles = LDX.IMMEDIATE.CYCLES
        self.e_reg = 'X'
        self.e_val = Expected_no_flag_byte.get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "LDX Immediate"

    def test_IMMEDIATE_zero_flags(self):
        self.cpu.write_byte(0x0200, LDX.IMMEDIATE.OPCODE)
        self.cpu.write_byte(0x0201, Expected_zero_flag_byte)

        self.cycles = LDX.IMMEDIATE.CYCLES
        self.e_reg = 'X'
        self.e_val = Expected_zero_flag_byte.get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "LDX Immediate"

    def test_IMMEDIATE_negative_flags(self):
        self.cpu.write_byte(0x0200, LDX.IMMEDIATE.OPCODE)
        self.cpu.write_byte(0x0201, Expected_negative_flag_byte)

        self.cycles = LDX.IMMEDIATE.CYCLES
        self.e_reg = 'X'
        self.e_val = Expected_negative_flag_byte.get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "LDX Immediate"

    def test_ZERO_PAGE_no_flags(self):
        self.cpu.write_byte(0x0200, LDX.ZERO_PAGE.OPCODE)
        self.cpu.write_byte(0x0201, 0x31)
        self.cpu.write_byte(0x0031, Expected_no_flag_byte)

        self.cycles = LDX.ZERO_PAGE.CYCLES
        self.e_reg = 'X'
        self.e_val = Expected_no_flag_byte.get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "LDX Zero Page"

    def test_ZERO_PAGE_zero_flags(self):
        self.cpu.write_byte(0x0200, LDX.ZERO_PAGE.OPCODE)
        self.cpu.write_byte(0x0201, 0x31)
        self.cpu.write_byte(0x0031, Expected_zero_flag_byte)

        self.cycles = LDX.ZERO_PAGE.CYCLES
        self.e_reg = 'X'
        self.e_val = Expected_zero_flag_byte.get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "LDX Zero Page"

    def test_ZERO_PAGE_negative_flags(self):
        self.cpu.write_byte(0x0200, LDX.ZERO_PAGE.OPCODE)
        self.cpu.write_byte(0x0201, 0x31)
        self.cpu.write_byte(0x0031, Expected_negative_flag_byte)

        self.cycles = LDX.ZERO_PAGE.CYCLES
        self.e_reg = 'X'
        self.e_val = Expected_negative_flag_byte.get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "LDX Zero Page"

    def test_ABSOLUTE_no_flag(self):
        self.cpu.write_byte(0x0200, LDX.ABSOLUTE.OPCODE)
        self.cpu.write_byte(0x0201, 0x31)
        self.cpu.write_byte(0x0202, 0xf0)
        self.cpu.write_byte(0xf031, Expected_no_flag_byte)

        self.cycles = LDX.ABSOLUTE.CYCLES
        self.e_reg = 'X'
        self.e_val = Expected_no_flag_byte.get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "LDX Absolute"

    def test_ABSOLUTE_zero_flag(self):
        self.cpu.write_byte(0x0200, LDX.ABSOLUTE.OPCODE)
        self.cpu.write_byte(0x0201, 0x31)
        self.cpu.write_byte(0x0202, 0xf0)
        self.cpu.write_byte(0xf031, Expected_zero_flag_byte)

        self.cycles = LDX.ABSOLUTE.CYCLES
        self.e_reg = 'X'
        self.e_val = Expected_zero_flag_byte.get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "LDX Absolute"

    def test_ABSOLUTE_negative_flag(self):
        self.cpu.write_byte(0x0200, LDX.ABSOLUTE.OPCODE)
        self.cpu.write_byte(0x0201, 0x31)
        self.cpu.write_byte(0x0202, 0xf0)
        self.cpu.write_byte(0xf031, Expected_negative_flag_byte)

        self.cycles = LDX.ABSOLUTE.CYCLES
        self.e_reg = 'X'
        self.e_val = Expected_negative_flag_byte.get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "LDX Absolute"

    def test_ZERO_PAGE_Y_no_flags(self):
        # using cpu method to ensure that Register Y contains correct data (LDY may not be working correctly)
        self.cpu.set_register_Y(0x05)

        self.cpu.write_byte(0x0200, LDX.ZERO_PAGE_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0x31)
        self.cpu.write_byte(0x0036, Expected_no_flag_byte)

        self.cycles = LDX.ZERO_PAGE_Y.CYCLES
        self.e_reg = 'X'
        self.e_val = Expected_no_flag_byte.get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "LDX Zero Page Y"

    def test_ZERO_PAGE_Y_zero_flag(self):
        # using cpu method to ensure that Register Y contains correct data (LDY may not be working correctly)
        self.cpu.set_register_Y(0x05)

        self.cpu.write_byte(0x0200, LDX.ZERO_PAGE_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0x31)
        self.cpu.write_byte(0x0036, Expected_zero_flag_byte)

        self.cycles = LDX.ZERO_PAGE_Y.CYCLES
        self.e_reg = 'X'
        self.e_val = Expected_zero_flag_byte.get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "LDX Zero Page Y"

    def test_ZERO_PAGE_Y_negative_flag(self):
        # using cpu method to ensure that Register Y contains correct data (LDY may not be working correctly)
        self.cpu.set_register_Y(0x05)

        self.cpu.write_byte(0x0200, LDX.ZERO_PAGE_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0x31)
        self.cpu.write_byte(0x0036, Expected_negative_flag_byte)

        self.cycles = LDX.ZERO_PAGE_Y.CYCLES
        self.e_reg = 'X'
        self.e_val = Expected_negative_flag_byte.get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "LDX Zero Page Y"

    def test_ABSOLUTE_Y_no_flag(self):
        # using cpu method to ensure that Register Y contains correct data (LDY may not be working correctly)
        self.cpu.set_register_Y(0x92)

        self.cpu.write_byte(0x0200, LDX.ABSOLUTE_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0x00)
        self.cpu.write_byte(0x0202, 0x20)
        self.cpu.write_byte(0x2092, Expected_no_flag_byte)

        self.cycles = LDX.ABSOLUTE_Y.CYCLES
        self.e_reg = 'X'
        self.e_val = Expected_no_flag_byte.get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "LDX Absolute X"

    def test_ABSOLUTE_Y_zero_flag(self):
        # using cpu method to ensure that Register Y contains correct data (LDY may not be working correctly)
        self.cpu.set_register_Y(0x92)

        self.cpu.write_byte(0x0200, LDX.ABSOLUTE_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0x00)
        self.cpu.write_byte(0x0202, 0x20)
        self.cpu.write_byte(0x2092, Expected_zero_flag_byte)

        self.cycles = LDX.ABSOLUTE_Y.CYCLES
        self.e_reg = 'X'
        self.e_val = Expected_zero_flag_byte.get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "LDX Absolute Y"

    def test_ABSOLUTE_Y_negative_flag(self):
        # using cpu method to ensure that Register Y contains correct data (LDY may not be working correctly)
        self.cpu.set_register_Y(0x92)

        self.cpu.write_byte(0x0200, LDX.ABSOLUTE_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0x00)
        self.cpu.write_byte(0x0202, 0x20)
        self.cpu.write_byte(0x2092, Expected_negative_flag_byte)

        self.cycles = LDX.ABSOLUTE_Y.CYCLES
        self.e_reg = 'X'
        self.e_val = Expected_negative_flag_byte.get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "LDX Absolute Y"

    def test_ABSOLUTE_Y_CROSSED_PAGE_no_flag(self):
        # using cpu method to ensure that Register Y contains correct data (LDY may not be working correctly)
        self.cpu.set_register_Y(0x92)

        self.cpu.write_byte(0x0200, LDX.ABSOLUTE_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0x6f)
        self.cpu.write_byte(0x0202, 0x20)
        self.cpu.write_byte(0x2101, Expected_no_flag_byte)

        self.cycles = LDX.ABSOLUTE_Y.CYCLES_CROSSED_PAGE
        self.e_reg = 'X'
        self.e_val = Expected_no_flag_byte.get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "LDX Absolute Y (crossed page)"

    def test_ABSOLUTE_Y_CROSSED_PAGE_zero_flag(self):
        # using cpu method to ensure that Register Y contains correct data (LDY may not be working correctly)
        self.cpu.set_register_Y(0x92)

        self.cpu.write_byte(0x0200, LDX.ABSOLUTE_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0x6f)
        self.cpu.write_byte(0x0202, 0x20)
        self.cpu.write_byte(0x2101, Expected_zero_flag_byte)

        self.cycles = LDX.ABSOLUTE_Y.CYCLES_CROSSED_PAGE
        self.e_reg = 'X'
        self.e_val = Expected_zero_flag_byte.get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "LDX Absolute Y (crossed page)"

    def test_ABSOLUTE_Y_CROSSED_PAGE_negative_flag(self):
        # using cpu method to ensure that Register Y contains correct data (LDY may not be working correctly)
        self.cpu.set_register_Y(0x92)

        self.cpu.write_byte(0x0200, LDX.ABSOLUTE_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0x6f)
        self.cpu.write_byte(0x0202, 0x20)
        self.cpu.write_byte(0x2101, Expected_negative_flag_byte)

        self.cycles = LDX.ABSOLUTE_Y.CYCLES_CROSSED_PAGE
        self.e_reg = 'X'
        self.e_val = Expected_negative_flag_byte.get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "LDX Absolute Y (crossed page)"

    def tearDown(self) -> None:
        e, a, m = execute_and_assert(self.cpu, self.cycles, self.e_reg, self.e_val,
                                     self.flags, self.test_name, self.mode)
        self.assertEqual(e, a, m)


class Test_LDY(unittest.TestCase):
    def setUp(self) -> None:
        self.cpu: CPU = T_Reset_cpu()

    def test_IMMEDIATE_no_flags(self):
        self.cpu.write_byte(0x0200, LDY.IMMEDIATE.OPCODE)
        self.cpu.write_byte(0x0201, Expected_no_flag_byte)

        self.cycles = LDY.IMMEDIATE.CYCLES
        self.e_reg = 'Y'
        self.e_val = Expected_no_flag_byte.get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "LDY Immediate"

    def test_IMMEDIATE_zero_flags(self):
        self.cpu.write_byte(0x0200, LDY.IMMEDIATE.OPCODE)
        self.cpu.write_byte(0x0201, Expected_zero_flag_byte)

        self.cycles = LDY.IMMEDIATE.CYCLES
        self.e_reg = 'Y'
        self.e_val = Expected_zero_flag_byte.get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "LDY Immediate"

    def test_IMMEDIATE_negative_flags(self):
        self.cpu.write_byte(0x0200, LDY.IMMEDIATE.OPCODE)
        self.cpu.write_byte(0x0201, Expected_negative_flag_byte)

        self.cycles = LDY.IMMEDIATE.CYCLES
        self.e_reg = 'Y'
        self.e_val = Expected_negative_flag_byte.get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "LDY Immediate"

    def test_ZERO_PAGE_no_flags(self):
        self.cpu.write_byte(0x0200, LDY.ZERO_PAGE.OPCODE)
        self.cpu.write_byte(0x0201, 0x31)
        self.cpu.write_byte(0x0031, Expected_no_flag_byte)

        self.cycles = LDY.ZERO_PAGE.CYCLES
        self.e_reg = 'Y'
        self.e_val = Expected_no_flag_byte.get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "LDY Zero Page"

    def test_ZERO_PAGE_zero_flags(self):
        self.cpu.write_byte(0x0200, LDY.ZERO_PAGE.OPCODE)
        self.cpu.write_byte(0x0201, 0x31)
        self.cpu.write_byte(0x0031, Expected_zero_flag_byte)

        self.cycles = LDY.ZERO_PAGE.CYCLES
        self.e_reg = 'Y'
        self.e_val = Expected_zero_flag_byte.get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "LDY Zero Page"

    def test_ZERO_PAGE_negative_flags(self):
        self.cpu.write_byte(0x0200, LDY.ZERO_PAGE.OPCODE)
        self.cpu.write_byte(0x0201, 0x31)
        self.cpu.write_byte(0x0031, Expected_negative_flag_byte)

        self.cycles = LDY.ZERO_PAGE.CYCLES
        self.e_reg = 'Y'
        self.e_val = Expected_negative_flag_byte.get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "LDY Zero Page"

    def test_ABSOLUTE_no_flag(self):
        self.cpu.write_byte(0x0200, LDY.ABSOLUTE.OPCODE)
        self.cpu.write_byte(0x0201, 0x31)
        self.cpu.write_byte(0x0202, 0xf0)
        self.cpu.write_byte(0xf031, Expected_no_flag_byte)

        self.cycles = LDY.ABSOLUTE.CYCLES
        self.e_reg = 'Y'
        self.e_val = Expected_no_flag_byte.get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "LDY Absolute"

    def test_ABSOLUTE_zero_flag(self):
        self.cpu.write_byte(0x0200, LDY.ABSOLUTE.OPCODE)
        self.cpu.write_byte(0x0201, 0x31)
        self.cpu.write_byte(0x0202, 0xf0)
        self.cpu.write_byte(0xf031, Expected_zero_flag_byte)

        self.cycles = LDY.ABSOLUTE.CYCLES
        self.e_reg = 'Y'
        self.e_val = Expected_zero_flag_byte.get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "LDY Absolute"

    def test_ABSOLUTE_negative_flag(self):
        self.cpu.write_byte(0x0200, LDY.ABSOLUTE.OPCODE)
        self.cpu.write_byte(0x0201, 0x31)
        self.cpu.write_byte(0x0202, 0xf0)
        self.cpu.write_byte(0xf031, Expected_negative_flag_byte)

        self.cycles = LDY.ABSOLUTE.CYCLES
        self.e_reg = 'Y'
        self.e_val = Expected_negative_flag_byte.get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "LDY Absolute"

    def test_ZERO_PAGE_X_no_flags(self):
        # using cpu method to ensure that Register X contains correct data (LDX may not be working correctly)
        self.cpu.set_register_X(0x05)

        self.cpu.write_byte(0x0200, LDY.ZERO_PAGE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0x31)
        self.cpu.write_byte(0x0036, Expected_no_flag_byte)

        self.cycles = LDY.ZERO_PAGE_X.CYCLES
        self.e_reg = 'Y'
        self.e_val = Expected_no_flag_byte.get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "LDY Zero Page X"

    def test_ZERO_PAGE_X_zero_flag(self):
        # using cpu method to ensure that Register X contains correct data (LDX may not be working correctly)
        self.cpu.set_register_X(0x05)

        self.cpu.write_byte(0x0200, LDY.ZERO_PAGE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0x31)
        self.cpu.write_byte(0x0036, Expected_zero_flag_byte)

        self.cycles = LDY.ZERO_PAGE_X.CYCLES
        self.e_reg = 'Y'
        self.e_val = Expected_zero_flag_byte.get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "LDY Zero Page X"

    def test_ZERO_PAGE_X_negative_flag(self):
        # using cpu method to ensure that Register X contains correct data (LDX may not be working correctly)
        self.cpu.set_register_X(0x05)

        self.cpu.write_byte(0x0200, LDY.ZERO_PAGE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0x31)
        self.cpu.write_byte(0x0036, Expected_negative_flag_byte)

        self.cycles = LDY.ZERO_PAGE_X.CYCLES
        self.e_reg = 'Y'
        self.e_val = Expected_negative_flag_byte.get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "LDY Zero Page X"

    def test_ABSOLUTE_X_no_flag(self):
        # using cpu method to ensure that Register X contains correct data (LDX may not be working correctly)
        self.cpu.set_register_X(0x92)

        self.cpu.write_byte(0x0200, LDY.ABSOLUTE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0x00)
        self.cpu.write_byte(0x0202, 0x20)
        self.cpu.write_byte(0x2092, Expected_no_flag_byte)

        self.cycles = LDY.ABSOLUTE_X.CYCLES
        self.e_reg = 'Y'
        self.e_val = Expected_no_flag_byte.get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "LDY Absolute X"

    def test_ABSOLUTE_X_zero_flag(self):
        # using cpu method to ensure that Register X contains correct data (LDX may not be working correctly)
        self.cpu.set_register_X(0x92)

        self.cpu.write_byte(0x0200, LDY.ABSOLUTE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0x00)
        self.cpu.write_byte(0x0202, 0x20)
        self.cpu.write_byte(0x2092, Expected_zero_flag_byte)

        self.cycles = LDY.ABSOLUTE_X.CYCLES
        self.e_reg = 'Y'
        self.e_val = Expected_zero_flag_byte.get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "LDY Absolute X"

    def test_ABSOLUTE_X_negative_flag(self):
        # using cpu method to ensure that Register X contains correct data (LDX may not be working correctly)
        self.cpu.set_register_X(0x92)

        self.cpu.write_byte(0x0200, LDY.ABSOLUTE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0x00)
        self.cpu.write_byte(0x0202, 0x20)
        self.cpu.write_byte(0x2092, Expected_negative_flag_byte)

        self.cycles = LDY.ABSOLUTE_X.CYCLES
        self.e_reg = 'Y'
        self.e_val = Expected_negative_flag_byte.get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "LDY Absolute X"

    def test_ABSOLUTE_X_CROSSED_PAGE_no_flag(self):
        # using cpu method to ensure that Register X contains correct data (LDX may not be working correctly)
        self.cpu.set_register_X(0x92)

        self.cpu.write_byte(0x0200, LDY.ABSOLUTE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0x6f)
        self.cpu.write_byte(0x0202, 0x20)
        self.cpu.write_byte(0x2101, Expected_no_flag_byte)

        self.cycles = LDY.ABSOLUTE_X.CYCLES_CROSSED_PAGE
        self.e_reg = 'Y'
        self.e_val = Expected_no_flag_byte.get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "LDY Absolute X (crossed page)"

    def test_ABSOLUTE_X_CROSSED_PAGE_zero_flag(self):
        # using cpu method to ensure that Register X contains correct data (LDX may not be working correctly)
        self.cpu.set_register_X(0x92)

        self.cpu.write_byte(0x0200, LDY.ABSOLUTE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0x6f)
        self.cpu.write_byte(0x0202, 0x20)
        self.cpu.write_byte(0x2101, Expected_zero_flag_byte)

        self.cycles = LDY.ABSOLUTE_X.CYCLES_CROSSED_PAGE
        self.e_reg = 'Y'
        self.e_val = Expected_zero_flag_byte.get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "LDY Absolute X (crossed page)"

    def test_ABSOLUTE_X_CROSSED_PAGE_negative_flag(self):
        # using cpu method to ensure that Register X contains correct data (LDX may not be working correctly)
        self.cpu.set_register_X(0x92)

        self.cpu.write_byte(0x0200, LDY.ABSOLUTE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0x6f)
        self.cpu.write_byte(0x0202, 0x20)
        self.cpu.write_byte(0x2101, Expected_negative_flag_byte)

        self.cycles = LDY.ABSOLUTE_X.CYCLES_CROSSED_PAGE
        self.e_reg = 'Y'
        self.e_val = Expected_negative_flag_byte.get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "LDY Absolute X (crossed page)"

    def tearDown(self) -> None:
        e, a, m = execute_and_assert(self.cpu, self.cycles, self.e_reg, self.e_val,
                                     self.flags, self.test_name, self.mode)
        self.assertEqual(e, a, m)


class Test_STA(unittest.TestCase):
    def setUp(self) -> None:
        self.cpu: CPU = T_Reset_cpu()

    def test_INDIRECT_X(self):
        # using cpu method to ensure that Register A contains correct data (LDA may not be working correctly)
        self.cpu.set_register_A(Expected_no_flag_byte)
        # using cpu method to ensure that Register X contains correct data (LDX may not be working correctly)
        self.cpu.set_register_X(0x05)

        self.cpu.write_byte(0x0200, STA.INDIRECT_X.OPCODE)
        self.cpu.write_byte(0x0201, 0x20)
        self.cpu.write_byte(0x0025, 0x05)
        self.cpu.write_byte(0x0026, 0x03)

        self.cycles = STA.INDIRECT_X.CYCLES
        self.e_reg = '0x0305'
        self.e_val = Expected_no_flag_byte.get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "STA Indirect X"

    def test_ZERO_PAGE(self):
        # using cpu method to ensure that Register A contains correct data (LDA may not be working correctly)
        self.cpu.set_register_A(Expected_no_flag_byte)

        self.cpu.write_byte(0x0200, STA.ZERO_PAGE.OPCODE)
        self.cpu.write_byte(0x0201, 0x20)

        self.cycles = STA.ZERO_PAGE.CYCLES
        self.e_reg = '0x0020'
        self.e_val = Expected_no_flag_byte.get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "STA Zero Page"

    def test_ABSOLUTE(self):
        # using cpu method to ensure that Register A contains correct data (LDA may not be working correctly)
        self.cpu.set_register_A(Expected_no_flag_byte)

        self.cpu.write_byte(0x0200, STA.ABSOLUTE.OPCODE)
        self.cpu.write_byte(0x0201, 0x20)
        self.cpu.write_byte(0x0202, 0x02)

        self.cycles = STA.ABSOLUTE.CYCLES
        self.e_reg = '0x0220'
        self.e_val = Expected_no_flag_byte.get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "STA Absolute"

    def test_INDIRECT_Y(self):
        # using cpu method to ensure that Register A contains correct data (LDA may not be working correctly)
        self.cpu.set_register_A(Expected_no_flag_byte)
        # using cpu method to ensure that Register Y contains correct data (LDY may not be working correctly)
        self.cpu.set_register_Y(0x05)

        self.cpu.write_byte(0x0200, STA.INDIRECT_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0x20)
        self.cpu.write_byte(0x0020, 0x05)
        self.cpu.write_byte(0x0021, 0x03)

        self.cycles = STA.INDIRECT_Y.CYCLES
        self.e_reg = '0x030a'
        self.e_val = Expected_no_flag_byte.get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "STA Indirect Y"

    def test_ZERO_PAGE_X(self):
        # using cpu method to ensure that Register A contains correct data (LDA may not be working correctly)
        self.cpu.set_register_A(Expected_no_flag_byte)
        # using cpu method to ensure that Register X contains correct data (LDX may not be working correctly)
        self.cpu.set_register_X(0x05)

        self.cpu.write_byte(0x0200, STA.ZERO_PAGE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0x20)
        self.cpu.write_byte(0x0025, Expected_no_flag_byte)

        self.cycles = STA.ZERO_PAGE_X.CYCLES
        self.e_reg = '0x0025'
        self.e_val = Expected_no_flag_byte.get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "STA Zero Page X"

    def test_ABSOLUTE_Y(self):
        # using cpu method to ensure that Register A contains correct data (LDA may not be working correctly)
        self.cpu.set_register_A(Expected_no_flag_byte)
        # using cpu method to ensure that Register Y contains correct data (LDY may not be working correctly)
        self.cpu.set_register_Y(0x05)

        self.cpu.write_byte(0x0200, STA.ABSOLUTE_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0xf0)
        self.cpu.write_byte(0x0202, 0x03)
        self.cpu.write_byte(0x03f5, Expected_no_flag_byte)

        self.cycles = STA.ABSOLUTE_Y.CYCLES
        self.e_reg = '0x03f5'
        self.e_val = Expected_no_flag_byte.get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "STA Absolute X"

    def test_ABSOLUTE_X(self):
        # using cpu method to ensure that Register A contains correct data (LDA may not be working correctly)
        self.cpu.set_register_A(Expected_no_flag_byte)
        # using cpu method to ensure that Register X contains correct data (LDX may not be working correctly)
        self.cpu.set_register_X(0x05)

        self.cpu.write_byte(0x0200, STA.ABSOLUTE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0xf0)
        self.cpu.write_byte(0x0202, 0x03)
        self.cpu.write_byte(0x03f5, Expected_no_flag_byte)

        self.cycles = STA.ABSOLUTE_X.CYCLES
        self.e_reg = '0x03f5'
        self.e_val = Expected_no_flag_byte.get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "STA Absolute X"

    def tearDown(self) -> None:
        e, a, m = execute_and_assert(self.cpu, self.cycles, self.e_reg, self.e_val,
                                     self.flags, self.test_name, self.mode)
        self.assertEqual(e, a, m)


class Test_STX(unittest.TestCase):
    def setUp(self) -> None:
        self.cpu: CPU = T_Reset_cpu()

    def test_ZERO_PAGE(self):
        # using cpu method to ensure that Register X contains correct data (LDX may not be working correctly)
        self.cpu.set_register_X(Expected_no_flag_byte)

        self.cpu.write_byte(0x0200, STX.ZERO_PAGE.OPCODE)
        self.cpu.write_byte(0x0201, 0x20)

        self.cycles = STX.ZERO_PAGE.CYCLES
        self.e_reg = '0x0020'
        self.e_val = Expected_no_flag_byte.get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "STX Zero Page"

    def test_ABSOLUTE(self):
        # using cpu method to ensure that Register X contains correct data (LDX may not be working correctly)
        self.cpu.set_register_X(Expected_no_flag_byte)

        self.cpu.write_byte(0x0200, STX.ABSOLUTE.OPCODE)
        self.cpu.write_byte(0x0201, 0x20)
        self.cpu.write_byte(0x0202, 0x02)

        self.cycles = STX.ABSOLUTE.CYCLES
        self.e_reg = '0x0220'
        self.e_val = Expected_no_flag_byte.get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "STX Absolute"

    def test_ZERO_PAGE_Y(self):
        # using cpu method to ensure that Register A contains correct data (LDA may not be working correctly)
        self.cpu.set_register_X(Expected_no_flag_byte)
        # using cpu method to ensure that Register X contains correct data (LDX may not be working correctly)
        self.cpu.set_register_Y(0x05)

        self.cpu.write_byte(0x0200, STX.ZERO_PAGE_Y.OPCODE)
        self.cpu.write_byte(0x0201, 0x20)
        self.cpu.write_byte(0x0025, Expected_no_flag_byte)

        self.cycles = STX.ZERO_PAGE_Y.CYCLES
        self.e_reg = '0x0025'
        self.e_val = Expected_no_flag_byte.get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "STX Zero Page Y"

    def tearDown(self) -> None:
        e, a, m = execute_and_assert(self.cpu, self.cycles, self.e_reg, self.e_val,
                                     self.flags, self.test_name, self.mode)
        self.assertEqual(e, a, m)


class Test_STY(unittest.TestCase):
    def setUp(self) -> None:
        self.cpu: CPU = T_Reset_cpu()

    def test_ZERO_PAGE(self):
        # using cpu method to ensure that Register X contains correct data (LDX may not be working correctly)
        self.cpu.set_register_Y(Expected_no_flag_byte)

        self.cpu.write_byte(0x0200, STY.ZERO_PAGE.OPCODE)
        self.cpu.write_byte(0x0201, 0x20)

        self.cycles = STY.ZERO_PAGE.CYCLES
        self.e_reg = '0x0020'
        self.e_val = Expected_no_flag_byte.get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "STY Zero Page"

    def test_ABSOLUTE(self):
        # using cpu method to ensure that Register X contains correct data (LDX may not be working correctly)
        self.cpu.set_register_Y(Expected_no_flag_byte)

        self.cpu.write_byte(0x0200, STY.ABSOLUTE.OPCODE)
        self.cpu.write_byte(0x0201, 0x20)
        self.cpu.write_byte(0x0202, 0x02)

        self.cycles = STY.ABSOLUTE.CYCLES
        self.e_reg = '0x0220'
        self.e_val = Expected_no_flag_byte.get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "STY Absolute"

    def test_ZERO_PAGE_X(self):
        # using cpu method to ensure that Register A contains correct data (LDA may not be working correctly)
        self.cpu.set_register_Y(Expected_no_flag_byte)
        # using cpu method to ensure that Register X contains correct data (LDX may not be working correctly)
        self.cpu.set_register_X(0x05)

        self.cpu.write_byte(0x0200, STY.ZERO_PAGE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0x20)
        self.cpu.write_byte(0x0025, Expected_no_flag_byte)

        self.cycles = STY.ZERO_PAGE_X.CYCLES
        self.e_reg = '0x0025'
        self.e_val = Expected_no_flag_byte.get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "STY Zero Page X"

    def tearDown(self) -> None:
        e, a, m = execute_and_assert(self.cpu, self.cycles, self.e_reg, self.e_val,
                                     self.flags, self.test_name, self.mode)
        self.assertEqual(e, a, m)


if __name__ == '__main__':
    unittest.main()
