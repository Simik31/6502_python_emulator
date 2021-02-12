# ##############################
#  Copyright (c) 2021          #
#                              #
#  Author: Martin Šimara       #
#  Last modified on 12.2.2021  #
# ##############################

import unittest
from Instructions.Stack_Operations import TSX, TXS, PHA, PHP, PLA, PLP
from Testing_constants import T_Reset_cpu, execute_and_assert
from Testing_constants import Expected_no_flag_byte, Expected_zero_flag_byte, Expected_negative_flag_byte


class Test_TSX(unittest.TestCase):
    def setUp(self) -> None:
        self.cpu = T_Reset_cpu()

    def test_IMPLIED_no_flag(self):
        self.cpu.set_SP(Expected_no_flag_byte)
        self.cpu.write_byte(0x0200, TSX.IMPLIED.OPCODE)

        self.cycles = TSX.IMPLIED.CYCLES
        self.e_reg = 'X'
        self.e_val = Expected_no_flag_byte.get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test TSX Implied"

    def test_IMPLIED_zero_flag(self):
        self.cpu.set_SP(Expected_zero_flag_byte)
        self.cpu.write_byte(0x0200, TSX.IMPLIED.OPCODE)

        self.cycles = TSX.IMPLIED.CYCLES
        self.e_reg = 'X'
        self.e_val = Expected_zero_flag_byte.get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test TSX Implied"

    def test_IMPLIED_negative_flag(self):
        self.cpu.set_SP(Expected_negative_flag_byte)
        self.cpu.write_byte(0x0200, TSX.IMPLIED.OPCODE)

        self.cycles = TSX.IMPLIED.CYCLES
        self.e_reg = 'X'
        self.e_val = Expected_negative_flag_byte.get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test TSX Implied"

    def tearDown(self) -> None:
        e, a, m = execute_and_assert(self.cpu, self.cycles, self.e_reg, self.e_val,
                                     self.flags, self.test_name, self.mode)
        self.assertEqual(e, a, m)


class Test_TXS(unittest.TestCase):
    def test_IMPLIED(self):
        cpu = T_Reset_cpu()
        cpu.set_register_X(Expected_no_flag_byte)
        cpu.write_byte(0x0200, TXS.IMPLIED.OPCODE)

        cycles = TXS.IMPLIED.CYCLES
        e_reg = 'SP'
        e_val = Expected_no_flag_byte.get_hex_value()
        mode = 1
        flags = cpu.get_register_F()
        test_name = "Test TXS Implied"

        e, a, m = execute_and_assert(cpu, cycles, e_reg, e_val, flags, test_name, mode)
        self.assertEqual(e, a, m)


class Test_PHA(unittest.TestCase):
    def test_IMPLIED(self):
        cpu = T_Reset_cpu()
        cpu.set_register_A(Expected_no_flag_byte)
        cpu.write_byte(0x0200, PHA.IMPLIED.OPCODE)

        cycles = PHA.IMPLIED.CYCLES
        e_reg = "%06x" % cpu.get_SP().get_value()
        e_val = Expected_no_flag_byte.get_hex_value()
        mode = 1
        flags = cpu.get_register_F()
        test_name = "Test PHA Implied"

        e, a, m = execute_and_assert(cpu, cycles, e_reg, e_val, flags, test_name, mode)
        self.assertEqual(e, a, m)


class Test_PHP(unittest.TestCase):
    def test_IMPLIED(self):
        cpu = T_Reset_cpu()
        cpu.set_register_F(Expected_no_flag_byte)
        cpu.write_byte(0x0200, PHP.IMPLIED.OPCODE)

        cycles = PHP.IMPLIED.CYCLES
        e_reg = "%06x" % cpu.get_SP().get_value()
        e_val = Expected_no_flag_byte.get_hex_value()
        mode = 1
        flags = cpu.get_register_F()
        test_name = "Test PHP Implied"

        e, a, m = execute_and_assert(cpu, cycles, e_reg, e_val, flags, test_name, mode)
        self.assertEqual(e, a, m)


class Test_PLA(unittest.TestCase):
    def setUp(self) -> None:
        self.cpu = T_Reset_cpu()

    def test_IMPLIED_no_flag(self):
        self.cpu.write_to_stack(Expected_no_flag_byte)
        self.cpu.write_byte(0x0200, PLA.IMPLIED.OPCODE)

        self.cycles = PLA.IMPLIED.CYCLES
        self.e_reg = "A"
        self.e_val = Expected_no_flag_byte.get_hex_value()
        self.mode = 1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test PLA Implied"

    def test_IMPLIED_zero_flag(self):
        self.cpu.write_to_stack(Expected_zero_flag_byte)
        self.cpu.write_byte(0x0200, PLA.IMPLIED.OPCODE)

        self.cycles = PLA.IMPLIED.CYCLES
        self.e_reg = "A"
        self.e_val = Expected_zero_flag_byte.get_hex_value()
        self.mode = 0
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test PLA Implied"

    def test_IMPLIED_negative_flag(self):
        self.cpu.write_to_stack(Expected_negative_flag_byte)
        self.cpu.write_byte(0x0200, PLA.IMPLIED.OPCODE)

        self.cycles = PLA.IMPLIED.CYCLES
        self.e_reg = "A"
        self.e_val = Expected_negative_flag_byte.get_hex_value()
        self.mode = -1
        self.flags = self.cpu.get_register_F()
        self.test_name = "Test PLA Implied"

    def tearDown(self) -> None:
        e, a, m = execute_and_assert(self.cpu, self.cycles, self.e_reg, self.e_val,
                                     self.flags, self.test_name, self.mode)
        self.assertEqual(e, a, m)


class Test_PLP(unittest.TestCase):
    def test_IMPLIED(self):
        cpu = T_Reset_cpu()
        cpu.write_to_stack(Expected_no_flag_byte)
        cpu.write_byte(0x0200, PLP.IMPLIED.OPCODE)

        cycles = PLP.IMPLIED.CYCLES
        e_reg = "F"
        e_val = Expected_no_flag_byte.get_hex_value()
        mode = 1
        flags = None
        test_name = "Test PLP Implied"

        e, a, m = execute_and_assert(cpu, cycles, e_reg, e_val, flags, test_name, mode)
        self.assertEqual(e, a, m)


if __name__ == '__main__':
    unittest.main()
