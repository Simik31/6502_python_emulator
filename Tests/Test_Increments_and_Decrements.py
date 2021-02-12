# ######################################
#  Copyright (c) 2021                  #
#                                      #
#  Author: Martin Šimara               #
#  Last modified on 04/02/2021, 17:55  #
# ######################################

import unittest
from Instructions.Increments_and_Decrements import INC, INX, INY, DEC, DEX, DEY
from Tests.Testing_constants import T_Reset_cpu, execute_and_assert, Expected_no_flag_byte, Expected_zero_flag_byte, \
    Expected_negative_flag_byte


class Test_INC(unittest.TestCase):
    def setUp(self) -> None:
        self.cpu = T_Reset_cpu()

    def test_ZERO_PAGE_no_flag(self):
        self.cpu.write_byte(0x001f, Expected_no_flag_byte - 1)
        self.cpu.write_byte(0x0200, INC.ZERO_PAGE.OPCODE)
        self.cpu.write_byte(0x0201, 0x1f)

        self.cycles = INC.ZERO_PAGE.CYCLES
        self.e_reg = '0x001f'
        self.e_val = Expected_no_flag_byte.get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test INC ZERO PAGE"

    def test_ZERO_PAGE_zero_flag(self):
        self.cpu.write_byte(0x001f, Expected_zero_flag_byte - 1)
        self.cpu.write_byte(0x0200, INC.ZERO_PAGE.OPCODE)
        self.cpu.write_byte(0x0201, 0x1f)

        self.cycles = INC.ZERO_PAGE.CYCLES
        self.e_reg = '0x001f'
        self.e_val = Expected_zero_flag_byte.get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test INC ZERO PAGE"

    def test_ZERO_PAGE_negative_flag(self):
        self.cpu.write_byte(0x001f, Expected_negative_flag_byte - 1)
        self.cpu.write_byte(0x0200, INC.ZERO_PAGE.OPCODE)
        self.cpu.write_byte(0x0201, 0x1f)

        self.cycles = INC.ZERO_PAGE.CYCLES
        self.e_reg = '0x001f'
        self.e_val = Expected_negative_flag_byte.get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test INC ZERO PAGE"

    def test_ABSOLUTE_no_flag(self):
        self.cpu.write_byte(0x0200, INC.ABSOLUTE.OPCODE)
        self.cpu.write_word(0x0201, 0x551f)
        self.cpu.write_byte(0x551f, Expected_no_flag_byte - 1)

        self.cycles = INC.ABSOLUTE.CYCLES
        self.e_reg = '0x551f'
        self.e_val = Expected_no_flag_byte.get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test INC ABSOLUTE"

    def test_ABSOLUTE_zero_flag(self):
        self.cpu.write_byte(0x0200, INC.ABSOLUTE.OPCODE)
        self.cpu.write_word(0x0201, 0x551f)
        self.cpu.write_byte(0x551f, Expected_zero_flag_byte - 1)

        self.cycles = INC.ABSOLUTE.CYCLES
        self.e_reg = '0x551f'
        self.e_val = Expected_zero_flag_byte.get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test INC ABSOLUTE"

    def test_ABSOLUTE_negative_flag(self):
        self.cpu.write_byte(0x0200, INC.ABSOLUTE.OPCODE)
        self.cpu.write_word(0x0201, 0x551f)
        self.cpu.write_byte(0x551f, Expected_negative_flag_byte - 1)

        self.cycles = INC.ABSOLUTE.CYCLES
        self.e_reg = '0x551f'
        self.e_val = Expected_negative_flag_byte.get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test INC ABSOLUTE"

    def test_ZERO_PAGE_X_no_flag(self):
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x001f, Expected_no_flag_byte - 1)
        self.cpu.write_byte(0x0200, INC.ZERO_PAGE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0x1a)

        self.cycles = INC.ZERO_PAGE_X.CYCLES
        self.e_reg = '0x001f'
        self.e_val = Expected_no_flag_byte.get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test INC ZERO PAGE X"

    def test_ZERO_PAGE_X_zero_flag(self):
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x001f, Expected_zero_flag_byte - 1)
        self.cpu.write_byte(0x0200, INC.ZERO_PAGE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0x1a)

        self.cycles = INC.ZERO_PAGE_X.CYCLES
        self.e_reg = '0x001f'
        self.e_val = Expected_zero_flag_byte.get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test INC ZERO PAGE X"

    def test_ZERO_PAGE_X_negative_flag(self):
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x001f, Expected_negative_flag_byte - 1)
        self.cpu.write_byte(0x0200, INC.ZERO_PAGE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0x1a)

        self.cycles = INC.ZERO_PAGE_X.CYCLES
        self.e_reg = '0x001f'
        self.e_val = Expected_negative_flag_byte.get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test INC ZERO PAGE X"

    def test_ABSOLUTE_X_no_flag(self):
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x0200, INC.ABSOLUTE_X.OPCODE)
        self.cpu.write_word(0x0201, 0x551a)
        self.cpu.write_byte(0x551f, Expected_no_flag_byte - 1)

        self.cycles = INC.ABSOLUTE_X.CYCLES
        self.e_reg = '0x551f'
        self.e_val = Expected_no_flag_byte.get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test INC ABSOLUTE X"

    def test_ABSOLUTE_X_zero_flag(self):
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x0200, INC.ABSOLUTE_X.OPCODE)
        self.cpu.write_word(0x0201, 0x551a)
        self.cpu.write_byte(0x551f, Expected_zero_flag_byte - 1)

        self.cycles = INC.ABSOLUTE_X.CYCLES
        self.e_reg = '0x551f'
        self.e_val = Expected_zero_flag_byte.get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test INC ABSOLUTE X"

    def test_ABSOLUTE_X_negative_flag(self):
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x0200, INC.ABSOLUTE_X.OPCODE)
        self.cpu.write_word(0x0201, 0x551a)
        self.cpu.write_byte(0x551f, Expected_negative_flag_byte - 1)

        self.cycles = INC.ABSOLUTE_X.CYCLES
        self.e_reg = '0x551f'
        self.e_val = Expected_negative_flag_byte.get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test INC ABSOLUTE X"

    def tearDown(self) -> None:
        e, a, m = execute_and_assert(self.cpu, self.cycles, self.e_reg, self.e_val,
                                     self.flags, self.test_name, self.mode)
        self.assertEqual(e, a, m)


class Test_INX(unittest.TestCase):
    def setUp(self) -> None:
        self.cpu = T_Reset_cpu()

    def test_IMPLIED_no_flag(self):
        self.cpu.set_register_X(Expected_no_flag_byte)
        self.cpu.write_byte(0x0200, INX.IMPLIED.OPCODE - 1)

        self.cycles = INX.IMPLIED.CYCLES
        self.e_reg = 'X'
        self.e_val = Expected_no_flag_byte.get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test INX Implied"

    def test_IMPLIED_zero_flag(self):
        self.cpu.set_register_X(Expected_zero_flag_byte - 1)
        self.cpu.write_byte(0x0200, INX.IMPLIED.OPCODE)

        self.cycles = INX.IMPLIED.CYCLES
        self.e_reg = 'X'
        self.e_val = Expected_zero_flag_byte.get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test INX Implied"

    def test_IMPLIED_negative_flag(self):
        self.cpu.set_register_X(Expected_negative_flag_byte - 1)
        self.cpu.write_byte(0x0200, INX.IMPLIED.OPCODE)

        self.cycles = INX.IMPLIED.CYCLES
        self.e_reg = 'X'
        self.e_val = Expected_negative_flag_byte.get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test INX Implied"

    def tearDown(self) -> None:
        e, a, m = execute_and_assert(self.cpu, self.cycles, self.e_reg, self.e_val,
                                     self.flags, self.test_name, self.mode)
        self.assertEqual(e, a, m)


class Test_INY(unittest.TestCase):
    def setUp(self) -> None:
        self.cpu = T_Reset_cpu()

    def test_IMPLIED_no_flag(self):
        self.cpu.set_register_Y(Expected_no_flag_byte - 1)
        self.cpu.write_byte(0x0200, INY.IMPLIED.OPCODE)

        self.cycles = INY.IMPLIED.CYCLES
        self.e_reg = 'Y'
        self.e_val = Expected_no_flag_byte.get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test INY Implied"

    def test_IMPLIED_zero_flag(self):
        self.cpu.set_register_Y(Expected_zero_flag_byte - 1)
        self.cpu.write_byte(0x0200, INY.IMPLIED.OPCODE)

        self.cycles = INY.IMPLIED.CYCLES
        self.e_reg = 'Y'
        self.e_val = Expected_zero_flag_byte.get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test INY Implied"

    def test_IMPLIED_negative_flag(self):
        self.cpu.set_register_Y(Expected_negative_flag_byte - 1)
        self.cpu.write_byte(0x0200, INY.IMPLIED.OPCODE)

        self.cycles = INY.IMPLIED.CYCLES
        self.e_reg = 'Y'
        self.e_val = Expected_negative_flag_byte.get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test INY Implied"

    def tearDown(self) -> None:
        e, a, m = execute_and_assert(self.cpu, self.cycles, self.e_reg, self.e_val,
                                     self.flags, self.test_name, self.mode)
        self.assertEqual(e, a, m)


class Test_DEC(unittest.TestCase):
    def setUp(self) -> None:
        self.cpu = T_Reset_cpu()

    def test_ZERO_PAGE_no_flag(self):
        self.cpu.write_byte(0x001f, Expected_no_flag_byte + 1)
        self.cpu.write_byte(0x0200, DEC.ZERO_PAGE.OPCODE)
        self.cpu.write_byte(0x0201, 0x1f)

        self.cycles = DEC.ZERO_PAGE.CYCLES
        self.e_reg = '0x001f'
        self.e_val = Expected_no_flag_byte.get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test DEC ZERO PAGE"

    def test_ZERO_PAGE_zero_page(self):
        self.cpu.write_byte(0x001f, Expected_zero_flag_byte + 1)
        self.cpu.write_byte(0x0200, DEC.ZERO_PAGE.OPCODE)
        self.cpu.write_byte(0x0201, 0x1f)

        self.cycles = DEC.ZERO_PAGE.CYCLES
        self.e_reg = '0x001f'
        self.e_val = Expected_zero_flag_byte.get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test DEC ZERO PAGE"

    def test_ZERO_PAGE_negative_flag(self):
        self.cpu.write_byte(0x001f, Expected_negative_flag_byte + 1)
        self.cpu.write_byte(0x0200, DEC.ZERO_PAGE.OPCODE)
        self.cpu.write_byte(0x0201, 0x1f)

        self.cycles = DEC.ZERO_PAGE.CYCLES
        self.e_reg = '0x001f'
        self.e_val = Expected_negative_flag_byte.get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test DEC ZERO PAGE"

    def test_ABSOLUTE_no_flag(self):
        self.cpu.write_byte(0x0200, DEC.ABSOLUTE.OPCODE)
        self.cpu.write_word(0x0201, 0x551f)
        self.cpu.write_byte(0x551f, Expected_no_flag_byte + 1)

        self.cycles = DEC.ABSOLUTE.CYCLES
        self.e_reg = '0x551f'
        self.e_val = Expected_no_flag_byte.get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test DEC ABSOLUTE"

    def test_ABSOLUTE_zero_flag(self):
        self.cpu.write_byte(0x0200, DEC.ABSOLUTE.OPCODE)
        self.cpu.write_word(0x0201, 0x551f)
        self.cpu.write_byte(0x551f, Expected_zero_flag_byte + 1)

        self.cycles = DEC.ABSOLUTE.CYCLES
        self.e_reg = '0x551f'
        self.e_val = Expected_zero_flag_byte.get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test DEC ABSOLUTE"

    def test_ABSOLUTE_negative_flag(self):
        self.cpu.write_byte(0x0200, DEC.ABSOLUTE.OPCODE)
        self.cpu.write_word(0x0201, 0x551f)
        self.cpu.write_byte(0x551f, Expected_negative_flag_byte + 1)

        self.cycles = DEC.ABSOLUTE.CYCLES
        self.e_reg = '0x551f'
        self.e_val = Expected_negative_flag_byte.get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test DEC ABSOLUTE"

    def test_ZERO_PAGE_X_no_flag(self):
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x001f, Expected_no_flag_byte + 1)
        self.cpu.write_byte(0x0200, DEC.ZERO_PAGE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0x1a)

        self.cycles = DEC.ZERO_PAGE_X.CYCLES
        self.e_reg = '0x001f'
        self.e_val = Expected_no_flag_byte.get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test DEC ZERO PAGE X"

    def test_ZERO_PAGE_X_zero_flag(self):
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x001f, Expected_zero_flag_byte + 1)
        self.cpu.write_byte(0x0200, DEC.ZERO_PAGE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0x1a)

        self.cycles = DEC.ZERO_PAGE_X.CYCLES
        self.e_reg = '0x001f'
        self.e_val = Expected_zero_flag_byte.get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test DEC ZERO PAGE X"

    def test_ZERO_PAGE_X_negative_flag(self):
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x001f, Expected_negative_flag_byte + 1)
        self.cpu.write_byte(0x0200, DEC.ZERO_PAGE_X.OPCODE)
        self.cpu.write_byte(0x0201, 0x1a)

        self.cycles = DEC.ZERO_PAGE_X.CYCLES
        self.e_reg = '0x001f'
        self.e_val = Expected_negative_flag_byte.get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test DEC ZERO PAGE X"

    def test_ABSOLUTE_X_no_flag(self):
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x0200, DEC.ABSOLUTE_X.OPCODE)
        self.cpu.write_word(0x0201, 0x551a)
        self.cpu.write_byte(0x551f, Expected_no_flag_byte + 1)

        self.cycles = DEC.ABSOLUTE_X.CYCLES
        self.e_reg = '0x551f'
        self.e_val = Expected_no_flag_byte.get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test DEC ABSOLUTE X"

    def test_ABSOLUTE_X_zero_flag(self):
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x0200, DEC.ABSOLUTE_X.OPCODE)
        self.cpu.write_word(0x0201, 0x551a)
        self.cpu.write_byte(0x551f, Expected_zero_flag_byte + 1)

        self.cycles = DEC.ABSOLUTE_X.CYCLES
        self.e_reg = '0x551f'
        self.e_val = Expected_zero_flag_byte.get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test DEC ABSOLUTE X"

    def test_ABSOLUTE_X_negative_flag(self):
        self.cpu.set_register_X(0x05)
        self.cpu.write_byte(0x0200, DEC.ABSOLUTE_X.OPCODE)
        self.cpu.write_word(0x0201, 0x551a)
        self.cpu.write_byte(0x551f, Expected_negative_flag_byte + 1)

        self.cycles = DEC.ABSOLUTE_X.CYCLES
        self.e_reg = '0x551f'
        self.e_val = Expected_negative_flag_byte.get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test DEC ABSOLUTE X"

    def tearDown(self) -> None:
        e, a, m = execute_and_assert(self.cpu, self.cycles, self.e_reg, self.e_val,
                                     self.flags, self.test_name, self.mode)
        self.assertEqual(e, a, m)


class Test_DEX(unittest.TestCase):
    def setUp(self) -> None:
        self.cpu = T_Reset_cpu()

    def test_IMPLIED_no_flag(self):
        self.cpu.set_register_X(Expected_no_flag_byte + 1)
        self.cpu.write_byte(0x0200, DEX.IMPLIED.OPCODE)

        self.cycles = DEX.IMPLIED.CYCLES
        self.e_reg = 'X'
        self.e_val = Expected_no_flag_byte.get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test DEX Implied"

    def test_IMPLIED_zero_flag(self):
        self.cpu.set_register_X(Expected_zero_flag_byte + 1)
        self.cpu.write_byte(0x0200, DEX.IMPLIED.OPCODE)

        self.cycles = DEX.IMPLIED.CYCLES
        self.e_reg = 'X'
        self.e_val = Expected_zero_flag_byte.get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test DEX Implied"

    def test_IMPLIED_negative_flag(self):
        self.cpu.set_register_X(Expected_negative_flag_byte + 1)
        self.cpu.write_byte(0x0200, DEX.IMPLIED.OPCODE)

        self.cycles = DEX.IMPLIED.CYCLES
        self.e_reg = 'X'
        self.e_val = Expected_negative_flag_byte.get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test DEX Implied"

    def tearDown(self) -> None:
        e, a, m = execute_and_assert(self.cpu, self.cycles, self.e_reg, self.e_val,
                                     self.flags, self.test_name, self.mode)
        self.assertEqual(e, a, m)


class Test_DEY(unittest.TestCase):
    def setUp(self) -> None:
        self.cpu = T_Reset_cpu()

    def test_IMPLIED_no_flag(self):
        self.cpu.set_register_Y(Expected_no_flag_byte + 1)
        self.cpu.write_byte(0x0200, DEY.IMPLIED.OPCODE)

        self.cycles = DEY.IMPLIED.CYCLES
        self.e_reg = 'Y'
        self.e_val = Expected_no_flag_byte.get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test DEY Implied"

    def test_IMPLIED_zero_flag(self):
        self.cpu.set_register_Y(Expected_zero_flag_byte + 1)
        self.cpu.write_byte(0x0200, DEY.IMPLIED.OPCODE)

        self.cycles = DEY.IMPLIED.CYCLES
        self.e_reg = 'Y'
        self.e_val = Expected_zero_flag_byte.get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test DEY Implied"

    def test_IMPLIED_negative_flag(self):
        self.cpu.set_register_Y(Expected_negative_flag_byte + 1)
        self.cpu.write_byte(0x0200, DEY.IMPLIED.OPCODE)

        self.cycles = DEY.IMPLIED.CYCLES
        self.e_reg = 'Y'
        self.e_val = Expected_negative_flag_byte.get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test DEY Implied"

    def tearDown(self) -> None:
        e, a, m = execute_and_assert(self.cpu, self.cycles, self.e_reg, self.e_val,
                                     self.flags, self.test_name, self.mode)
        self.assertEqual(e, a, m)


if __name__ == '__main__':
    unittest.main()
