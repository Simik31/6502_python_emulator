# ##############################
#  Copyright (c) 2021          #
#                              #
#  Author: Martin Šimara       #
#  Last modified on 12.2.2021  #
# ##############################

import unittest
from CPU import CPU
from Instructions.Register_Transfers import TAX, TAY, TXA, TYA
from Testing_constants import T_Reset_cpu, execute_and_assert
from Testing_constants import Expected_no_flag_byte, Expected_zero_flag_byte, Expected_negative_flag_byte


class Test_TAX(unittest.TestCase):
    def setUp(self) -> None:
        self.cpu: CPU = T_Reset_cpu()

    def test_IMPLIED_no_flag(self):
        self.cpu.set_register_A(Expected_no_flag_byte)

        self.cpu.write_byte(0x0200, TAX.IMPLIED.OPCODE)

        self.cycles = TAX.IMPLIED.CYCLES
        self.e_reg = 'X'
        self.e_val = Expected_no_flag_byte.get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test TAX Implied"

    def test_IMPLIED_zero_flag(self):
        self.cpu.set_register_A(Expected_zero_flag_byte)

        self.cpu.write_byte(0x0200, TAX.IMPLIED.OPCODE)

        self.cycles = TAX.IMPLIED.CYCLES
        self.e_reg = 'X'
        self.e_val = Expected_zero_flag_byte.get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test TAX Implied"

    def test_IMPLIED_negative_flag(self):
        self.cpu.set_register_A(Expected_negative_flag_byte)

        self.cpu.write_byte(0x0200, TAX.IMPLIED.OPCODE)

        self.cycles = TAX.IMPLIED.CYCLES
        self.e_reg = 'X'
        self.e_val = Expected_negative_flag_byte.get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test TAX Implied"

    def tearDown(self) -> None:
        e, a, m = execute_and_assert(self.cpu, self.cycles, self.e_reg, self.e_val,
                                     self.flags, self.test_name, self.mode)
        self.assertEqual(e, a, m)


class Test_TAY(unittest.TestCase):
    def setUp(self) -> None:
        self.cpu: CPU = T_Reset_cpu()

    def test_IMPLIED_no_flag(self):
        self.cpu.set_register_A(Expected_no_flag_byte)

        self.cpu.write_byte(0x0200, TAY.IMPLIED.OPCODE)

        self.cycles = TAY.IMPLIED.CYCLES
        self.e_reg = 'Y'
        self.e_val = Expected_no_flag_byte.get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test TAY Implied"

    def test_IMPLIED_zero_flag(self):
        self.cpu.set_register_A(Expected_zero_flag_byte)

        self.cpu.write_byte(0x0200, TAY.IMPLIED.OPCODE)

        self.cycles = TAY.IMPLIED.CYCLES
        self.e_reg = 'Y'
        self.e_val = Expected_zero_flag_byte.get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test TAY Implied"

    def test_IMPLIED_negative_flag(self):
        self.cpu.set_register_A(Expected_negative_flag_byte)

        self.cpu.write_byte(0x0200, TAY.IMPLIED.OPCODE)

        self.cycles = TAY.IMPLIED.CYCLES
        self.e_reg = 'Y'
        self.e_val = Expected_negative_flag_byte.get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test TAY Implied"

    def tearDown(self) -> None:
        e, a, m = execute_and_assert(self.cpu, self.cycles, self.e_reg, self.e_val,
                                     self.flags, self.test_name, self.mode)
        self.assertEqual(e, a, m)


class Test_TXA(unittest.TestCase):
    def setUp(self) -> None:
        self.cpu: CPU = T_Reset_cpu()

    def test_IMPLIED_no_flag(self):
        self.cpu.set_register_X(Expected_no_flag_byte)

        self.cpu.write_byte(0x0200, TXA.IMPLIED.OPCODE)

        self.cycles = TXA.IMPLIED.CYCLES
        self.e_reg = 'A'
        self.e_val = Expected_no_flag_byte.get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test TXA Implied"

    def test_IMPLIED_zero_flag(self):
        self.cpu.set_register_X(Expected_zero_flag_byte)

        self.cpu.write_byte(0x0200, TXA.IMPLIED.OPCODE)

        self.cycles = TXA.IMPLIED.CYCLES
        self.e_reg = 'A'
        self.e_val = Expected_zero_flag_byte.get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test TXA Implied"

    def test_IMPLIED_negative_flag(self):
        self.cpu.set_register_X(Expected_negative_flag_byte)

        self.cpu.write_byte(0x0200, TXA.IMPLIED.OPCODE)

        self.cycles = TXA.IMPLIED.CYCLES
        self.e_reg = 'A'
        self.e_val = Expected_negative_flag_byte.get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test TXA Implied"

    def tearDown(self) -> None:
        e, a, m = execute_and_assert(self.cpu, self.cycles, self.e_reg, self.e_val,
                                     self.flags, self.test_name, self.mode)
        self.assertEqual(e, a, m)


class Test_TYA(unittest.TestCase):
    def setUp(self) -> None:
        self.cpu: CPU = T_Reset_cpu()

    def test_IMPLIED_no_flag(self):
        self.cpu.set_register_Y(Expected_no_flag_byte)

        self.cpu.write_byte(0x0200, TYA.IMPLIED.OPCODE)

        self.cycles = TYA.IMPLIED.CYCLES
        self.e_reg = 'A'
        self.e_val = Expected_no_flag_byte.get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test TYA Implied"

    def test_IMPLIED_zero_flag(self):
        self.cpu.set_register_Y(Expected_zero_flag_byte)

        self.cpu.write_byte(0x0200, TYA.IMPLIED.OPCODE)

        self.cycles = TYA.IMPLIED.CYCLES
        self.e_reg = 'A'
        self.e_val = Expected_zero_flag_byte.get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test TYA Implied"

    def test_IMPLIED_negative_flag(self):
        self.cpu.set_register_Y(Expected_negative_flag_byte)

        self.cpu.write_byte(0x0200, TYA.IMPLIED.OPCODE)

        self.cycles = TYA.IMPLIED.CYCLES
        self.e_reg = 'A'
        self.e_val = Expected_negative_flag_byte.get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test TYA Implied"

    def tearDown(self) -> None:
        e, a, m = execute_and_assert(self.cpu, self.cycles, self.e_reg, self.e_val,
                                     self.flags, self.test_name, self.mode)
        self.assertEqual(e, a, m)


if __name__ == '__main__':
    unittest.main()
